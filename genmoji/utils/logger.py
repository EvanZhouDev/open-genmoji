import logging


def setup_logger(name: str) -> logging.Logger:
    """
    Sets up a logger instance with a set log format
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create a formatter for the log messages
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    # Create a console handler for the log messages
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    # logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


logger = setup_logger(__name__)