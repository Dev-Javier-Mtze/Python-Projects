from typing import Protocol, runtime_checkable


@runtime_checkable
class CreateOrder(Protocol):

    def get_order(self):
        pass
