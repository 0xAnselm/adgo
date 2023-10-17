import logging
from logging.handlers import RotatingFileHandler
from logging import StreamHandler


def configure_logger():
    logger = logging.getLogger('werkzeug')
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        handler = StreamHandler()
        handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger
