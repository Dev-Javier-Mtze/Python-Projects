import requests

from poetry_demo.domain.ports import CreateOrder


class RetrieveResponseHttp(CreateOrder):
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_order(self):
        response = requests.get(f"{self.base_url}")
        data = response.json()
        return data
