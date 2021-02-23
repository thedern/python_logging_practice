
dict_log_config = {
        "version": 1,
        "handlers": {
            "fileHandler": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "myFormatter",
                "encoding": "utf-8",
                "backupCount": 5,
                "maxBytes": 10485760,
                "filename": "logs/dic_logger.log",
            }
        },
        "loggers": {
            "main_logger": {
                "handlers": ["fileHandler"],
                "level": "INFO",
            },
            "utility_logger": {
                "handlers": ["fileHandler"],
                "level": "INFO"
            },
        },
        "formatters": {
            "myFormatter": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
    }