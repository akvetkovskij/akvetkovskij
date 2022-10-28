from typing import Optional, List

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from Homework_10.models import create_session, Product


class CRUDProduct(object):

    @staticmethod
    @create_session
    def add(product: Product, session=None):
        session.add(product)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(product)
            return product

    @staticmethod
    @create_session
    def get(product_id: int, session=None) -> Optional[Product]:
        product = session.execute(
            select(Product)
            .where(Product.id == product_id)
        )
        product = product.first()
        if product:
            return product[0]

    @staticmethod
    @create_session
    def all(session=None) -> List[Product]:
        products = session.execute(
            select(Product)
            .order_by(Product.id)
        )
        return [product[0] for product in products]

    @staticmethod
    @create_session
    def update(product: Product, session=None) -> bool:
        product = product.__dict__
        del product['_sa_instance_state']
        session.execute(
            update(Product)
            .where(Product.id == product.get('id'))
            .values(
                **product
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
    def delete(product_id: int, session=None) -> None:
        session.execute(
            delete(Product)
            .where(Product.id == product_id)
        )
        session.commite()


# new = Product(
#     title='Sweets',
#     descr='Tasty',
#     category_id=2
# )
# print(CRUDProduct.add(product=new))
# all_in_product = CRUDProduct.all()
# for product in CRUDProduct.all():
#     print(product.title)
