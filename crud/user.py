from typing import Optional, List

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from Homework_10.models import User, create_session


class CRUDUser(object):

    @staticmethod
    @create_session
    def add(user: User, session=None):
        session.add(user)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(user)
            return user

    @staticmethod
    @create_session
    def get(user_id: int, session=None) -> Optional[User]:
        user = session.execute(
            select(User)
            .where(User.id == user_id)
        )
        user = user.first()
        if user:
            return user[0]

    @staticmethod
    @create_session
    def all(session=None) -> List[User]:
        users = session.execute(
            select(User)
            .order_by(User.id)
        )
        return [user[0] for user in users]

    @staticmethod
    @create_session
    def update(user: User, session=None) -> bool:
        user = user.__dict__
        del user['_sa_instance_state']
        session.execute(
            update(User)
            .where(User.id == user.get('id'))
            .values(
                **user
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
    def delete(user_id: int, session=None) -> None:
        session.execute(
            delete(User)
            .where(User.id == user_id)
        )
        session.commite()
