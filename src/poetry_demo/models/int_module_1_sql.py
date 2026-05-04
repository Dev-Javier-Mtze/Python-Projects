import os
from abc import abstractmethod

from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
PROJECT_ROOT = os.path.dirname(BASE_DIR)
print(PROJECT_ROOT)
DATABASE_URL = f"sqlite:///{os.path.join(PROJECT_ROOT, 'data', 'mi_base.db')}"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()


class Main(Base):
    __abstract__ = True

    @abstractmethod
    def db(self):
        pass


class User(Main):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship("Order", back_populates="user")

    def db(self):
        return f"User: {self.id}"


class Order(Main):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user_order = Column(String, nullable=False)

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

    def db(self):
        return f"Order: {self.id}"


class OrderItem(Main):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
    discount = Column(Boolean, default=False)

    order = relationship("Order", back_populates="items")

    def db(self):
        return f"OrderItem: {self.id}"


Base.metadata.create_all(engine)
