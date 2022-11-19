from typing import Optional, List

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

# from Homework_10.models import create_session, Category
from Homework_10.models import create_async_session, Category


class CRUDCategory(object):

    @staticmethod
    # @create_session
    @create_async_session
    async def add(category: Category, session: AsyncSession = None) -> Optional[Category]:
        """
        For adding some information in database
        :param session: it is decorator
        :param category: name
        :return: Category
        """
        session.add(category)
        try:
            await session.commit()
        except IntegrityError:
            return None
        else:
            await session.refresh(category)
            return category

    @staticmethod
    # @create_session
    @create_async_session
    async def get(category_id: int, session: AsyncSession = None) -> Optional[Category]:
        """
        For getting information about category with id
        :param session: it is decorator
        :param category_id: id
        :return: Category
        """
        category = await session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return category[0]

    @staticmethod
    # @create_session
    @create_async_session
    async def all(session: AsyncSession = None) -> List[Category]:
        categories = await session.execute(
            select(Category)
            .order_by(Category.id)
        )
        return [category[0] for category in categories]  # для распаковки

    @staticmethod
    # @create_session
    @create_async_session
    async def update(category: Category, session: AsyncSession = None) -> bool:
        """
        This function for update information in table 'Category'
        :param session: It is a decorator
        :param category: Catgory.id???
        :return: Categoru.id before update
        """
        category = category.__dict__
        del category['_sa_instance_state']
        await session.execute(
            update(Category)
            .where(Category.id == category.get('id'))
            .values(
                **category
            )
        )
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    # @create_session
    @create_async_session
    async def delete(category_id: int, session: AsyncSession = None) -> None:
        """
        For deleting Category
        :param session: it is decorator
        :param category_id: id category for delete
        :return: Nothing
        """
        await session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        await session.commit()


# CRUDCategory.delete(category_id=1)
# new = Category(
#     name='Food',
#     descr='descr'
# )
# CRUDCategory.add(category=new)
