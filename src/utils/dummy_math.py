# dummy module for use with my logger examples
import logging
from logging import config
from src.conf.logging_dictionary import dict_log_config

logging.config.dictConfig(dict_log_config)
logger = logging.getLogger("utility_logger")


def add(x, y):
    return x + y


class Adder(object):
    """
    Object that does the same as the function above, just for shits and grins
    """
    def add_numbers(self, a, b):
        logger.info('adding numbers in my method')
        return a + b
