# import logging

# # Configuración básica
# logging.basicConfig(
#     level=logging.DEBUG,  # Se registran todos los niveles desde DEBUG hacia arriba
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

import logging
import logging.config

# Diccionario de configuración
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "default",
            "filename": "app.log",
            "mode": "a",
        },
    },
    "root": {"handlers": ["console", "file"], "level": "DEBUG"},
}


def setup_logging():
    """Inicializa la configuración de logging."""
    logging.config.dictConfig(LOGGING_CONFIG)
