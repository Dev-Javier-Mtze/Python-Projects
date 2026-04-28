import random
from dataclasses import dataclass
from decimal import Decimal

from pydantic import BaseModel, Field


@dataclass(order=True)
class Order:
    quantity: int
    discount_applied: bool = False
    sub_total: Decimal = 0
    total: float = 0

    @property
    def total_cost(self) -> float:
        self.total = self.quantity * Decimal("2.99")
        return self.total

    @property
    def apply_sub_total(self) -> float:
        if self.discount_applied:
            self.sub_total = self.less
        else:
            self.sub_total = self.total
        return round(self.sub_total, 2)

    @property
    def less(self) -> float:
        return self.total_cost * Decimal("0.90")

    @property
    def discount(self) -> bool:
        return self.discount_applied

    @discount.setter
    def discount(self, value: bool):
        self.discount_applied = value


class OrderOut(BaseModel):
    quantity: int = Field(..., gt=0, lt=100)
    sub_total: float = Field(..., gt=-1)
    discount: bool = False
    total: float = Field(..., gt=0)


class OrderIn(BaseModel):
    quantity: int = Field(..., gt=0, lt=100)
    sub_total: float = Field(..., gt=-1)
    discount: bool = False
    total: float = Field(..., gt=0)


def main():
    price = Decimal("2.99")
    quantity_input = int(
        input("Hello!! Welcome to our donut shop, how many donuts do you want?\n")
    )

    print(f"Your order: {quantity_input} donuts. Price per donut: ${price}")

    my_order = Order(quantity_input, False)
    print(f"The total cost of your order is: ${my_order.total_cost:.2f}")

    last_order_quanity = random.randint(1, 10)
    last_order = Order(last_order_quanity, price, False)
    print(
        f"Last week you order was {last_order.quantity} donuts. And a total of ${last_order.total_cost:.2f}"
    )

    if last_order.quantity > my_order.quantity:
        print(f"Your total is ${my_order.total_cost:.2f}")
    elif last_order.quantity < my_order.quantity:
        print(
            "Oh I see that you bought more donuts this time, let me give you a discount."
        )
        my_order.discount = True
        print(
            f"Your total was ${my_order.total_cost:.2f}, "
            f"but with your discount, your new total is: ${my_order.less:.2f}"
        )
    else:
        print("You always buy the same amount of donuts, such a nice person")

    return my_order


def complete_order(order: Order):
    new_order = OrderOut(
        quantity=order.quantity,
        sub_total=order.total,
        discount=order.discount_applied,
        total=order.apply_sub_total,
    )
    return new_order


def retrieve_order(order):
    new_order = OrderIn(**order.model_dump())
    return new_order


order = main()
order_out = complete_order(order)
print(f"Order out: {order_out}")
order_in = retrieve_order(order_out)
print(order_in)
