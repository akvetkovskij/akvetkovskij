from typing import Optional, List

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from Homework_10.models import Status, create_session


class CRUDStatus(object):

    @staticmethod
    @create_session
    def add(status: Status, session=None):
        session.add(status)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(status)
            return status

    @staticmethod
    @create_session
    def get(status_id: int, session=None) -> Optional[Status]:
        status = session.execute(
            select(Status)
            .where(Status.id == status_id)
        )
        status = status.first()
        if status:
            return status[0]

    @staticmethod
    @create_session
    def all(session=None) -> List[Status]:
        statuses = session.execute(
            select(Status)
            .order_by(Status.id)
        )
        return [status[0] for status in statuses]

    @staticmethod
    @create_session
    def update(status: Status, session=None) -> bool:
        status = status.__dict__
        del status['_sa_instance_state']
        session.execute(
            update(Status)
            .where(Status.id == status.get('id'))
            .values(
                **status
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
    def delete(status_id: int, session=None) -> None:
        session.execute(
            delete(Status)
            .where(Status.id == status_id)
        )
        session.commite()
