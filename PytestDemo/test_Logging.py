import logging


def test_logging_demo():
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)  # filehandler object
    logger.setLevel(logging.DEBUG)
    logger.debug("Debug line")
    logger.info("Info line")
    logger.warning('Warning Logs')
    logger.error('error line')
    logger.critical('critical line')


