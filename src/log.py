import logging


def custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s [z%(name)s] [%(levelname)s]: %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
