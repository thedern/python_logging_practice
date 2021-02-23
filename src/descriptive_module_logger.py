import logging
from src.utils import dummy_math


# -----------------------------------------------
# more descriptive module logger
# includes a formatter that tells us more details
# better than the simple module logger
# but, logging is still instantiated in main()
# ------------------------------------------------


def main():
    """
    main entry point of application
    """

    # create logger instance and set level
    log = logging.getLogger("exampleApp")
    log.setLevel(logging.INFO)

    # create log file handler and format
    fh = logging.FileHandler("logs/descriptive_logger.log")
    # date/time, name of logger, log-level, message
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)

    # add file handler to log object
    log.addHandler(fh)

    log.info("program started")
    result = dummy_math.add(7, 8)
    log.info("done!")


if __name__ == "__main__":
    main()
