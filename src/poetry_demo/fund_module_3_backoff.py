import random
import time
from contextlib import contextmanager

import backoff
import requests
from requests.exceptions import HTTPError

from poetry_demo.utils import logging_console_file

from poetry_demo.config import Settings

settings = Settings()

print(settings.http_url)

def fatal_error(details):
    logger.warning(f"Giving up after {details['tries']} tries.")
    return


@backoff.on_exception(
    backoff.expo,
    (requests.exceptions.RequestException, requests.exceptions.HTTPError),
    max_tries=3,
    on_giveup=fatal_error,
)
def llamar_api(url):
    logger.debug(f"Intentando llamar: {url}")

    response = requests.get(url)
    if response.status_code == 500:
        raise HTTPError("ERRO")
    return response


def url():
    url = random.choice([settings.http_url, settings.error_http_url])
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
    logger.debug(f"{description}: {end - start:.4f} segundos")


if __name__ == "__main__":
    logger = logging_console_file.logging_file("module_3_backoff")
    logger.info(" - - - - - - Start of the test - - - - - - ")
    with timer("API call ends at"):
        url = url()
        try:
            logger.debug(llamar_api(url))
        except Exception:
            logger.debug("Error calling the endpoint")
