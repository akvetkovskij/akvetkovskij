from typing import Optional, List

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from Homework_10.models import create_session, Order


class CRUDOrder(object):

    @staticmethod
    @create_session
    def add(order: Order, session=None):
        session.add(order)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(order)
            return order

    @staticmethod
    @create_session
    def get(order_id: int, session=None) -> Optional[Order]:
        order = session.execute(
            select(Order)
            .where(Order.id == order_id)
        )
        order = order.first()
        if order:
            return order[0]

    @staticmethod
    @create_session
    def all(session=None) -> List[Order]:
        orders = session.execute(
            select(Order)
            .order_by(Order.id)
        )
        return [order[0] for order in orders]

    @staticmethod
    @create_session
    def update(order: Order, session=None) -> bool:
        order = order.__dict__
        del order['_sa_instance_state']
        session.execute(
            update(Order)
            .where(Order.id == order.get('id'))
            .values(
                **order
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
    def delete(order_id: int, session=None) -> None:
        session.execute(
            delete(Order)
            .where(Order.id == order_id)
        )
        session.commit()


# new_order = Order(
#     descr='Trying to add'
# )
# CRUDOrder.add(order=new_order)
