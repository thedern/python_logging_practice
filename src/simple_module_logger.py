import logging
from src.utils import dummy_math


# -----------------------------------------------
# simple logging from module to a single file.
# Not very flexible for large projects
# 'main' is doing the logging via importing the logger, then passing messages to logger
# ----------------------------------------------


def main():
    """
    the main entry point to the application
    :return:
    """

    # create log file
    logging.basicConfig(
        filename="logs/simple_module_logger.log", filemode="w", level=logging.INFO
    )
    # create instance of the logger (will not use default 'root' logger), instead made our own
    log = logging.getLogger("mathlogger")

    # start logging information
    log.info("Program Started")
    result = dummy_math.add(7, 8)
    log.info(result)
    log.info("Done!")


if __name__ == "__main__":
    main()
