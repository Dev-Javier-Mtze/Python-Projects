import logging
import random

import httpx
import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from poetry_demo.utils import base_dir, logging_console_file

logger = logging.getLogger("module_7_httpx")


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=0.5),
    retry=retry_if_exception_type((httpx.ConnectTimeout, httpx.ReadTimeout)),
)
def api_call():
    logger.debug("Intentando")
    time = random.uniform(0.1, 0.3)
    client = httpx.Client(timeout=httpx.Timeout(time))
    response = client.get("https://httpbin.org/get")
    logger.debug(response)


if __name__ == "__main__":
    logger = logging_console_file.logging_file("module_7_httpx")
    logger.info(" - - - - - - Start of the test - - - - - - ")

try:
    api_call()
except Exception:
    logger.warning("An error ocurred")


url = "https://storage.to/HoSCYRqwn"
ruta_salida = f"{base_dir.url_dir()}/data/dog.zip"

logger.debug("Streaming a disco")
with requests.get(url, stream=True) as respuesta:
    with open(ruta_salida, "wb") as archivo:
        for bloque in respuesta.iter_content(chunk_size=8192):
            if bloque:
                archivo.write(bloque)

logger.debug(f"File downloaded successfully: {ruta_salida}")
