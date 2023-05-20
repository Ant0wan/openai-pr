import logging


def init(config: dict):
    format = '[%(asctime)s] %(levelname)-7s %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    if config['logs']['profile'] == 'action':
        logging.basicConfig(level=logging.INFO, format=format, datefmt=datefmt)
    else:
        logging.basicConfig(
            level=logging.DEBUG,
            format=format,
            datefmt=datefmt)
