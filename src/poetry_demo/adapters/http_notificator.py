from poetry_demo.domain.ports import CreateOrder


class Notification(CreateOrder):
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_order(self):
        print(f"We are currently trying to get the information from {self.base_url}")
