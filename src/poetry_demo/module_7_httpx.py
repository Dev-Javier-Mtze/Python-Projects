import logging
import os
import random

import httpx
import requests
from logging_config import setup_logging
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

setup_logging()
logger = logging.getLogger("module_7_httpx")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=0.5),
    retry=retry_if_exception_type((httpx.ConnectTimeout, httpx.ReadTimeout)),
)
def api_call():
    print("Intentando")
    time = random.uniform(0.1, 0.3)
    client = httpx.Client(timeout=httpx.Timeout(time))
    response = client.get("https://httpbin.org/get")
    print(response)


try:
    api_call()
except Exception:
    print("An error ocurred")


url = "https://storage.to/HoSCYRqwn"
ruta_salida = f"{BASE_DIR}/data/dog.zip"

with requests.get(url, stream=True) as respuesta:
    respuesta.raise_for_status()
    with open(ruta_salida, "wb") as archivo:
        for bloque in respuesta.iter_content(chunk_size=8192):
            if bloque:
                archivo.write(bloque)

print("File downloaded successfully:", ruta_salida)
logger.debug(f"File downloaded successfully: {ruta_salida}")
