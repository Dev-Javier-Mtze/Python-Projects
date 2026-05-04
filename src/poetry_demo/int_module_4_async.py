import asyncio
import time
from contextlib import contextmanager

import httpx
import requests

# Lista de URLs de ejemplo
URLS = [
    "https://httpbin.org/get",
    "https://httpbin.org/get",
    "https://httpbin.org/get",
    "https://httpbin.org/get",
]
id = 1
# Límite de concurrencia con semáforo
semaphore = asyncio.Semaphore(4)


async def sema(client, url):
    global id
    async with semaphore:  # Limita el número de tareas concurrentes
        print(f"Fetching: {url} number {id}")
        with timer("API call ends at"):
            id = id + 1
            response = await client.get(url)
        return response.json()


async def fetch(client: httpx.AsyncClient, url: str) -> dict:
    try:
        return await sema(client, url)
    except Exception:
        print("Error calling the endpoint")


async def main():
    async with httpx.AsyncClient(timeout=10.0) as client:
        tasks = [fetch(client, url) for url in URLS]
        results = await asyncio.gather(*tasks)
        # print(results)
        return results


def main2():
    [fetch2(url) for url in URLS]


def fetch2(url):
    with timer("API call ends at"):
        response = requests.get(url)
        print(response)


@contextmanager
def timer(description):
    start = time.time()
    yield
    end = time.time()
    print(f"{description}: {end - start:.4f} segundos")


if __name__ == "__main__":
    asyncio.run(main())
    print("----------")
    main2()
