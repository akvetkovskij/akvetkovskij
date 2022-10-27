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


new_order = Order(
    descr='Trying to add'
)
CRUDOrder.add(order=new_order)
