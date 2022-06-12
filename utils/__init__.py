import time
from logger import logger


def calculate_time(function_name):
    """calculates time taken by function to execution"""

    def wrapper_function(*arg, **kwargs):
        start_time = time.time()
        result = function_name(*arg, **kwargs)
        end_time = time.time()
        logger.info(
            f"{function_name.__name__} executed in {(end_time-start_time):.4f}s"
        )
        return result

    return wrapper_function
