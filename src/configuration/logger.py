import logging
import logging.config


class Logger:

    def __init__(self, config: dict):
        self.__profile = config['logs']['profile']
        self.__logging = config['logs']['logging']
        logging.config.fileConfig(self.__logging)
        logger = logging.getLogger(self.__profile)
        logging.debug("Logger profile: %s", self.__profile)
