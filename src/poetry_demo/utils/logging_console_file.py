import logging
import os

from poetry_demo.utils import base_dir

URL = f"{os.path.join(base_dir.url_dir(), 'logs', 'app.log')}"


def logging_file(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    format_console = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    format_file = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(format_console)

    file_handler = logging.FileHandler(URL)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(format_file)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
