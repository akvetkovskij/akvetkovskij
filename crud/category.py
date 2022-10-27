from typing import Optional, List

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from Homework_10.models import create_session, Category


class CRUDCategory(object):

    @staticmethod
    @create_session
    def add(category: Category, session=None) -> Optional[Category]:
        """
        For adding some information in database
        :param session: it is decorator
        :param category: name
        :return: Category
        """
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(category)
            return category

    @staticmethod
    @create_session
    def get(category_id: int, session=None) -> Optional[Category]:
        """
        For getting information about category with id
        :param session: it is decorator
        :param category_id: id
        :return: Category
        """
        category = session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return category[0]

    @staticmethod
    @create_session
    def all(session=None) -> List[Category]:
        categories = session.execute(
            select(Category)
            .order_by(Category.id)
        )
        return [category[0] for category in categories]  # для распаковки

    @staticmethod
    @create_session
    def update(category: Category, session=None) -> bool:
        """
        This function for update information in table 'Category'
        :param session: It is a decorator
        :param category: Catgory.id???
        :return: Categoru.id before update
        """
        category = category.__dict__
        del category['_sa_instance_state']
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

    @staticmethod
    @create_session
    def delete(category_id: int, session=None) -> None:
        """
        For deleting Category
        :param session: it is decorator
        :param category_id: id category for delete
        :return: Nothing
        """
        session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        session.commit()


# CRUDCategory.delete(category_id=1)