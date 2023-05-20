from logging import RootLogger
from src.utils.logger import LoggerResolver


def test_create_instance_logger():
    logger = LoggerResolver.get_logger()

    assert logger is not None
    assert isinstance(logger, RootLogger)
