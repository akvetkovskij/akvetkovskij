from typing import Optional, List

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from Homework_10.models import OrderItem, create_session


class CRUDOrderItem(object):

    @staticmethod
    @create_session
    def add(order_item: OrderItem, session=None):
        session.add(order_item)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(order_item)
            return order_item

    @staticmethod
    @create_session
    def get(order_item_id: int, session=None) -> Optional[OrderItem]:
        order_item = session.execute(
            select(OrderItem)
            .where(OrderItem.id == order_item_id)
        )
        order_item = order_item.first()
        if order_item:
            return order_item[0]

    @staticmethod
    @create_session
    def all(session=None) -> List[OrderItem]:
        order_items = session.execute(
            select(OrderItem)
            .order_by(OrderItem.id)
        )
        return [order_item[0] for order_item in order_items]

    @staticmethod
    @create_session
    def update(order_item: OrderItem, session=None) -> bool:
        order_item = order_item.__dict__
        del order_item['_sa_instance_state']
        session.execute(
            update(OrderItem)
            .where(OrderItem.id == order_item.get('id'))
            .values(
                **order_item
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
    def delete(order_item_id: int, session=None) -> None:
        session.execute(
            delete(OrderItem)
            .where(OrderItem.id == order_item_id)
        )
        session.commite()
