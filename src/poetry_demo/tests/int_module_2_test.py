import pytest
from hypothesis import given
from hypothesis import strategies as st

from poetry_demo.fund_module_2_games import validate_game_id
from poetry_demo.fund_module_4_order import Order


@given(st.integers(min_value=1, max_value=9999))
def test_valid_ids_return_value(n):
    assert validate_game_id(int(n)) == n


@given(st.text())
def test_valid_ids_rejects_strings(n):
    with pytest.raises(TypeError):
        validate_game_id(n)


def test_order_quantity():
    order = Order(10)
    assert order.quantity == 10


def test_order_total_cost():
    order = Order(10)
    order.total_cost
    assert round(order.total, 2) == 29.90


def test_order_apply_sub_total():
    order = Order(10, True)
    order.apply_sub_total
    assert round(order.sub_total, 2) == 26.91


def test_order_less():
    order = Order(10)
    assert round(order.discount_calc, 2) == 26.91
