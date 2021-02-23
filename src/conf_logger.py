import logging
import logging.config
from src.utils import dummy_math


# -------------------------------------------------
# loads logging from a config file
# logging is setup in the conf file and we just import the file,
# and then create the logging instance ('log')
# -------------------------------------------------


def main():

    logging.config.fileConfig("conf/logging.conf")
    log = logging.getLogger("mathApp")

    log.info("Program started")
    result = dummy_math.add(7, 8)
    log.info(result)
    log.info("Done!")


if __name__ == "__main__":
    main()
