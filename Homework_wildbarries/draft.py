from typing import Optional, List

from sqlalchemy import create_engine, select, update, delete  # create_engine для создания переменной подключения к БД
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from Homework_10.settings import DATABASE_URL  # импорт ссылки подключения к БД
from Homework_10.models import Category

engine = create_engine(DATABASE_URL)  # переменная подключения к БД
Session = sessionmaker(bind=engine)  # связь сесии с engine


def add_category(category: Category) -> Optional[Category]:
    """
    For adding some information in database
    :param category: name
    :return: Category
    """
    with Session() as session:
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(category)
            return category


def get_category(category_id: int) -> Optional[Category]:
    """
    For getting information about category with id
    :param category_id: id
    :return: Category
    """
    with Session() as session:
        category = session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return category[0]


def all_categories() -> List[Category]:
    with Session() as session:
        categories = session.execute(
            select(Category)
            .order_by(Category.id)
        )
        return [category[0] for category in categories]  # для распаковки


def update_category(category: Category) -> bool:
    category = category.__dict__
    del category['_sa_instance_state']
    with Session() as session:
        session.execute(
            update(Category)
            .where(Category.id == category.get('id'))
            .values(
                **category
            )
        )
    try:
        session.commit()
    except IntegrityError:
        return False
    else:
        return True


def delete_category(category_id: int) -> None:
    with Session() as session:
        session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        session.commit()