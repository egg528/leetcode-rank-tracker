import logging
from tracker.meta.singleton import SingletonMeta


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.logger = self._setup_logger()

    @staticmethod
    def _setup_logger() -> logging.Logger:
        logger = logging.getLogger('global_logger')
        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        console_handler.setFormatter(formatter)

        if not logger.hasHandlers():
            logger.addHandler(console_handler)

        return logger

    @staticmethod
    def info(msg: str) -> None:
        logger = Logger().logger
        logger.info(msg)

    @staticmethod
    def warn(msg: str) -> None:
        logger = Logger().logger
        logger.warning(msg)

    @staticmethod
    def error(msg: str) -> None:
        logger = Logger().logger
        logger.error(msg)