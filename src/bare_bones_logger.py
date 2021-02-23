import logging

# with logging set to INFO, debug messages will not be recorded
# basicConfig allows us to capture the logs, else logging is to stdout
logging.basicConfig(filename="logs/bare_bones.log", filemode="w", level=logging.INFO)
logging.debug("This is a DEBUG message")
logging.info("Informational message")
logging.error("An error happened")


# logging the entire tracebock to file
# 'ex' is the 'name' of the logger for the sake of the logfile and is for the most part arbitrary
log = logging.getLogger("ex")
try:
    raise RuntimeError
except Exception as err:
    log.exception("Error!")
