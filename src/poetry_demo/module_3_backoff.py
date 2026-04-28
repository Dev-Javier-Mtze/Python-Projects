import logging
import random
import time
from contextlib import contextmanager

import backoff
import requests
from requests.exceptions import HTTPError

from logging_config import setup_logging

setup_logging()
logger = logging.getLogger("module_3_backoff")


def fatal_error(details):
    print(f"Giving up after {details['tries']} tries.")
    return


@backoff.on_exception(
    backoff.expo,
    (requests.exceptions.RequestException, requests.exceptions.HTTPError),
    max_tries=3,
    on_giveup=fatal_error,
)
def llamar_api(url):
    print("Intentando llamada...")
    logger.debug(f"Intentando llamar: {url}")

    response = requests.get(url)
    if response.status_code == 500:
        raise HTTPError("ERRO")
    return response


def url():
    url = random.choice(["https://httpbin.org/get", "https://httpbin.org/status/500"])
    print(url)
    return url


def batch_generator(data, time):
    for i in range(0, len(data), time):
        yield data[i : i + time]


@contextmanager
def timer(description):
    start = time.time()
    yield
    end = time.time()
    datos = list(range(int(start), int(end)))
    for lote in batch_generator(datos, 5):
        print(lote)
    print(f"{description}: {end - start:.4f} segundos")


with timer("API call ends at"):
    url = url()
    time.sleep(4)
    try:
        print(llamar_api(url))
    except Exception:
        print("Error calling the endpoint")

datos = list(range(1, 21))
# for lote in batch_generator(datos, 5):
#     print(lote)
