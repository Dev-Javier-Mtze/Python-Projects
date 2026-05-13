import random
from dataclasses import dataclass
from decimal import Decimal
from typing import Union

from pydantic import BaseModel, Field

from poetry_demo.utils import logging_console_file

class Order(BaseModel):
    quantity: int
    discount_applied: bool = False
    price: float = 2.99

    @property
    def total_cost(self) -> float:
        return round(self.quantity * 2.99, 2)
    
    @property
    def sub_total(self) -> float:
        return self.discount_calc if self.discount_applied else self.total_cost

    @property
    def discount_calc(self) -> float:
        return round(self.total_cost * 0.90, 2)

    @property
    def discount(self) -> bool:
        return self.discount_applied

    @discount.setter
    def discount(self, value: bool):
        self.discount_applied = value

class OrderCreated:
    def my_order(self, donut_amount):
        logger.debug(f"Your order is being created: {donut_amount} donuts.")


class OrderAmount:
    def discountApplied(self, actual_quantity, last_quantity) -> Order:
        my_order = Order(quantity=actual_quantity)
        last_order = Order(quantity=last_quantity)
        
        logger.debug(f"The total cost of your order is: ${my_order.total_cost:.2f}")
        logger.debug(
            f"Last week you order was {last_order.quantity} donuts. And a total of ${last_order.total_cost:.2f}"
        )
        if last_order.quantity > my_order.quantity:
            logger.debug(f"Your total is ${my_order.total_cost:.2f}")
        elif last_order.quantity < my_order.quantity:
            logger.debug(
                "Oh I see that you bought more donuts this time, let me give you a discount."
            )
            my_order.discount_applied = True
            logger.debug(
                f"Your total was ${my_order.total_cost:.2f}, "
                f"but with your discount, your new total is: ${my_order.sub_total:.2f}"
            )
        else:
            logger.debug("You always buy the same amount of donuts, such a nice person")

        return my_order

class OrderOut(BaseModel):
    quantity: int = Field(..., gt=0, lt=100)
    sub_total: Union[float, Decimal] = Field(..., gt=-1)
    discount: bool = False
    total: Union[float, Decimal] = Field(..., gt=0)

class UnitOfWork:
    def __init__(self):
        self.orders = []

    def save_order(self, order: Order):
        self.orders.append(f"Order with {order.quantity} donuts was purchased.")
    
    def retrieve_orders(self):
        return self.orders


class Presenter:
    def complete_order(self, order: Order):
        return order.model_dump()

    def show_orders(self, orders):
        for order in orders:
            logger.debug(f"Orders saved: {order}")



def main():
    quantity_input = int(
        input("Hello!! Welcome to our donut shop, how many donuts do you want?\n")
    )
    last_order_quanity = random.randint(1, 10)
    order_created = OrderCreated()
    order_created.my_order(quantity_input)
    order_made = OrderAmount()
    order = order_made.discountApplied(quantity_input, last_order_quanity)
    order = OrderOut(
        quantity=order.quantity,
        sub_total=order.total_cost,
        discount=order.discount_applied,
        total=order.sub_total,
    )

    unit = UnitOfWork()
    unit.save_order(order)
    orders = unit.retrieve_orders()
    order_out = Presenter()
    order_presented = order_out.complete_order(order)
    order_out.show_orders(orders)
    logger.debug(f"Order out: {order_presented}")



if __name__ == "__main__":
    logger = logging_console_file.logging_file("fund_module_4_order")
    logger.info(" - - - - - - Start of the test - - - - - - ")
    order = main()
