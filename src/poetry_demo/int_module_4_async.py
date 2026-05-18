import asyncio
import logging
import time
from contextlib import contextmanager

import httpx
import requests

from poetry_demo.config import Settings
from poetry_demo.utils import logging_console_file

logger = logging.getLogger("module_7_httpx")
settings = Settings()

URLS = [
    settings.http_url,
    settings.http_url,
    settings.http_url,
    settings.http_url,
]
id = 1
semaphore = asyncio.Semaphore(2)


async def sema(client, url):
    global id
    async with semaphore:
        print(f"Fetching: {url} number {id}")
        with timer("API call ends at"):
            id = id + 1
            response = await client.get(url)
        return response.json()


async def fetch(client: httpx.AsyncClient, url: str) -> dict:
    try:
        return await sema(client, url)
    except Exception:
        logger.warning("Error calling the endpoint")
        return {}


async def main():
    async with httpx.AsyncClient(timeout=10.0) as client:
        tasks = [fetch(client, url) for url in URLS]
        results = await asyncio.gather(*tasks)
        return results


def main2():
    [fetch2(url) for url in URLS]


def fetch2(url):
    with timer("API call ends at"):
        response = requests.get(url)
        logger.debug(response)


@contextmanager
def timer(description):
    start = time.time()
    yield
    end = time.time()
    logger.debug(f"{description}: {end - start:.4f} segundos")


if __name__ == "__main__":
    logger = logging_console_file.logging_file("int_module_4_async")
    logger.info(" - - - - - - Start of the test - - - - - - ")
    asyncio.run(main())
    logger.debug("----------")
    main2()
