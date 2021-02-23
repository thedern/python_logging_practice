import logging
import logging.config
from src.conf.logging_dictionary import dict_log_config
from src.utils.dummy_math import Adder


def main():

    logging.config.dictConfig(dict_log_config)
    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger(__name__)
    logger = logging.getLogger("main_logger")
    logger.info("Program Started")

    adder_instance = Adder()
    result = adder_instance.add_numbers(7, 8)

    logger.info(result)
    logger.info("Program Done")


if __name__ == "__main__":
    main()
