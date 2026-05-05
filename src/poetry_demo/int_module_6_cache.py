from abc import abstractmethod
from functools import cache

import requests

from poetry_demo.utils import logging_console_file


@cache
def infinity(n):
    for x in range(0, n):
        logger.debug(x * n)
    return "Same result, we use cache"


class Port:
    @abstractmethod
    def get_data(self) -> float:
        pass


class Middle:
    def receive_data(self) -> float:
        url = "https://httpbin.org/get"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data


class Adapter(Port):
    def __init__(self, service: Middle):
        self.service = service

    def get_data(self):
        data = self.service.receive_data()
        return data


def main():
    service = Middle()
    adapter = Adapter(service)
    res = adapter.get_data()
    logger.debug(f"Response: {res['origin']}")


if __name__ == "__main__":
    logger = logging_console_file.logging_file("int_module_6_cache")
    logger.info(" - - - - - - Start of the test - - - - - - ")
    main()
    logger.debug(infinity(12))
    logger.debug(infinity(12))
