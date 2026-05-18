# orders_cli/cli.py
import os
import random

import typer
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from poetry_demo.models.int_module_1_sql import Order, OrderItem, User
from poetry_demo.utils import base_dir

DATABASE_URL = f"sqlite:///{os.path.join(base_dir.url_dir(), 'data', 'mi_base.db')}"
app = typer.Typer(help="CLI para gestionar Orders")
API_URL = "https://api.example.com/orders"

engine = create_engine(DATABASE_URL, echo=True)


@app.command()
def list_orders():
    with Session(engine) as session:
        usuarios = session.query(User).all()
        for u in usuarios:
            typer.echo(f"Name: {u.name} Id: {u.id}")


@app.command()
def add_user_orders(name: str, user_id: int, order_id: int):
    user_order = random.choice(["small", "medium", "large"])
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
            order_id=order_id,
            name=name,
            quantity=quantity,
            total=total,
            discount=discount,
        )
        session.add(order_item)
        session.commit()


@app.command()
def delete_user_orders(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
            typer.echo(f"Deleted user {user_id}")
        else:
            typer.echo(f"User {user_id} not found")
