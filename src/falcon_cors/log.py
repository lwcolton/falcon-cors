import logging

def get_default_logger():
    logger = logging.getLogger("falcon_cors")
    logger.setLevel(logging.INFO)
    logger.propogate = False
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
    return logger


