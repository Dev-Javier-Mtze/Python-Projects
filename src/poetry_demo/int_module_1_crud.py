import os
import random

from models.int_module_1_sql import Order, OrderItem, User
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
PROJECT_ROOT = os.path.dirname(BASE_DIR)
print(PROJECT_ROOT)
DATABASE_URL = (
    f"sqlite:///{os.path.join(PROJECT_ROOT, 'poetry_demo/data', 'mi_base.db')}"
)
engine = create_engine(DATABASE_URL, echo=True)

name = input("Give me a name:\n")
user_id = int(input("Give me a number:\n"))
user_order = random.choice(["small", "medium", "large"])
order_id = int(input("Give me an id:\n"))
quantity = random.randint(1, 1000)
total = random.randint(1, 1000)
discount = random.choice([True, False])

# Insertar datos
with Session(engine) as session:
    nuevo_usuario = User(name=name)
    session.add(nuevo_usuario)
    session.commit()

with Session(engine) as session:
    order = Order(user_id=user_id, user_order=user_order)
    session.add(order)
    session.commit()

with Session(engine) as session:
    order = OrderItem(
        order_id=order_id, name=name, quantity=quantity, total=total, discount=discount
    )
    session.add(order)
    session.commit()

# Consultar datos
with Session(engine) as session:
    usuarios = session.query(User).all()
    for u in usuarios:
        print(u.id, u.name)


with Session(engine) as session:
    order_item = session.query(OrderItem).all()
    for u in order_item:
        print(u.id, u.order_id, u.name, u.quantity, u.total, u.discount)
