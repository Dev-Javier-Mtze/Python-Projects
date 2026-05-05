import os
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from poetry_demo.models.int_module_1_sql import Order, OrderItem, User
from poetry_demo.utils import base_dir, logging_console_file

DATABASE_URL = f"sqlite:///{os.path.join(base_dir.url_dir(), 'data', 'mi_base.db')}"
if __name__ == "__main__":
    logger = logging_console_file.logging_file("int_module_1_crud")
    logger.info(" - - - - - - Start of the test - - - - - - ")

engine = create_engine(DATABASE_URL, echo=True)

name = input("Give me a name:\n")
user_id = int(input("Give me a number:\n"))
user_order = random.choice(["small", "medium", "large"])
order_id = int(input("Give me an id:\n"))
quantity = random.randint(1, 1000)
total = random.randint(1, 1000)
discount = random.choice([True, False])

with Session(engine) as session:
    nuevo_usuario = User(name=name)
    session.add(nuevo_usuario)
    session.commit()

with Session(engine) as session:
    order = Order(user_id=user_id, user_order=user_order)
    session.add(order)
    session.commit()

with Session(engine) as session:
    order_item = OrderItem(
        order_id=order_id, name=name, quantity=quantity, total=total, discount=discount
    )
    session.add(order_item)
    session.commit()

with Session(engine) as session:
    usuarios = session.query(User).all()
    for u in usuarios:
        logger.debug(f"{u.id}, {u.name}")


with Session(engine) as session:
    list_of_order_item = session.query(OrderItem).all()
    for items in list_of_order_item:
        logger.debug(
            f"{items.id}, {items.order_id}, {items.name}, {items.quantity}, {items.total}, {items.discount}"
        )
