from sqlalchemy.orm import declarative_base, sessionmaker

from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy import create_engine  # create_engine для создания переменной подключения к БД
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

# from Homework_10.settings import DATABASE_URL  # импорт ссылки подключения к БД
from Homework_10.settings import DATABASE_ASYNC_URL # импорт асинхронной ссылки подключения к БД

Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(24), nullable=False, unique=True)    # nullable=False - не может быть пустым, если True - то может
    descr = Column(VARCHAR(140), nullable=True)


class Product(Base):
    __tablename__: str = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(36), nullable=False, unique=True)
    descr = Column(VARCHAR(140))
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class User(Base):
    __tablename__: str = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(24), nullable=False)
    email = Column(VARCHAR(24), nullable=False, unique=True)


class Status(Base):
    __tablename__: str = 'statuses'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(10), nullable=False, unique=True)


class Order(Base):
    __tablename__: str = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    status_id = Column(Integer, ForeignKey('statuses.id', ondelete='CASCADE'), nullable=False)
    descr = Column(VARCHAR(140), nullable=True)


class OrderItem(Base):
    __tablename__: str = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)


engine = create_async_engine(DATABASE_ASYNC_URL)  # переменная подключения к БД
# engine = create_engine(DATABASE_URL) # синхронное подключение к БД
Session = sessionmaker(bind=engine)  # связь сесии с engine


def create_async_session(func):
    """
    Assync decorator for any function
    :param func: function
    :return: function before decorator with open session
    """
    async def wrapper(**kwargs):
        async with AsyncSession(bind=engine) as session:
            return await func(**kwargs, session=session)
    return wrapper


# def create_session(func):
#     """synchronous decorator"""
#     def wrapper(**kwargs):
#         with Session() as session:
#             return func(**kwargs, session=session)
#     return wrapper
