from logging import getLogger, INFO


class LoggerResolver:

    __instance = None

    @classmethod
    def get_logger(cls):
        if cls.__instance is None:
            cls.__instance = getLogger()
            cls.__instance.setLevel(INFO)
        return cls.__instance
