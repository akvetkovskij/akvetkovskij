from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from sqlalchemy import create_engine, select, update, delete  # create_engine для создания переменной подключения к БД
from sqlalchemy.orm import sessionmaker

from settings import DATABASE_URL  # импорт ссылки подключения к БД


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


class OrderItem(Base):
    __tablename__: str = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)


engine = create_engine(DATABASE_URL)  # переменная подключения к БД
Session = sessionmaker(bind=engine)  # связь сесии с engine


def create_session(func):
    """
    Decorator for any function
    :param func: function
    :return: function before decorator with open session
    """
    def wrapper(**kwargs):
        with Session() as session:
            return func(**kwargs, session=session)
    return wrapper
