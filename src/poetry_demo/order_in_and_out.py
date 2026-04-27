from decimal import Decimal

from pydantic import BaseModel, Field


class Order(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1, max_length=30)
    quantity: int = Field(..., gt=0)
    cost: Decimal = Field(..., gt=Decimal(0), decimal_places=2)

    def show_order(self) -> str:
        return print(self.id, self.name, self.quantity, self.cost)


task1 = Order(id=1, name="Chicken", quantity=2, cost=19.99)
task1.show_order()
