import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from poetry_demo.models.int_module_1_sql import Base, Order, OrderItem, User


@pytest.fixture
def test_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def test_create_user(test_session):
    user = User(name="Alice")
    test_session.add(user)
    test_session.commit()

    assert user.id is not None


def test_create_order_with_items(test_session):
    user = User(name="Bob")
    test_session.add(user)
    test_session.commit()

    order = Order(user_id=user.id, user_order="837")
    test_session.add(order)
    test_session.commit()

    item = OrderItem(
        order_id=order.id, name="Laptop", quantity=1, total=1200.0, discount=True
    )
    test_session.add(item)
    test_session.commit()

    assert order.items[0].name == "Laptop"
