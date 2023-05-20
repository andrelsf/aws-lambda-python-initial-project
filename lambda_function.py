
from src.handler import EventProcessor
from src.utils.logger import LoggerResolver

logger = LoggerResolver.get_logger()


def lambda_handler(event, context):
    logger.info(f"Context: {context}")
    result = EventProcessor.process(event)
    return result
