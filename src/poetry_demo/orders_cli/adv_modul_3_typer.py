# orders_cli/cli.py
import typer
import requests
import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from poetry_demo.utils import base_dir, logging_console_file
from poetry_demo.models.int_module_1_sql import Order, OrderItem, User

DATABASE_URL = f"sqlite:///{os.path.join(base_dir.url_dir(), 'data', 'mi_base.db')}"
app = typer.Typer(help="CLI para gestionar Orders")
API_URL = "https://api.example.com/orders"

engine = create_engine(DATABASE_URL, echo=True)

@app.command("list")
def list_orders():
    typer.echo(f"Hello world")
    # """Listar todas las órdenes"""
    # response = requests.get(API_URL)
    # if response.status_code == 200:
    #     for order in response.json():
    #         typer.echo(f"ID: {order['id']} | Cliente: {order['customer']} | Total: {order['total']}")
    # else:
    #     typer.echo("Error al listar órdenes")
    # with Session(engine) as session:
    #     usuarios = session.query(User).all()
    #     for u in usuarios:
    #         # logger.debug(f"{u.id}, {u.name}")
    #          typer.echo(f"ID: {u['id']} | Name: {u['name']}")
    # else:
