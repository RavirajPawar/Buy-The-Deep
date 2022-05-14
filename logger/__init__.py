import logging
from Singleton import Singleton


class CustomLogger(metaclass=Singleton):
    """logger class which crates logging class object"""

    def __init__(self, ) -> None:
        self.custom_logger = logging.getLogger("__name__")
        stream_handler = logging.StreamHandler()
        log_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(log_formatter)
        self.custom_logger.addHandler(stream_handler)


logger = CustomLogger().custom_logger
