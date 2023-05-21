"""
This module provides a logging configuration initializer based on a provided
configuration dictionary.

The module includes a single function, 'init', that can be called to
initialize the logging configuration. The 'init' function takes a configuration
dictionary as an argument and configures the logging module accordingly.
The configuration dictionary should contain a 'logs' key, which itself should
contain a 'profile' key specifying the desired logging profile.
If the 'profile' value is 'action', the logging level will be set to INFO.
Otherwise, the logging level will be set to DEBUG.

Example usage:
--------------
config = {
    'logs': {
        'profile': 'action'
    }
}

init(config)

"""
import logging


def init(config: dict):
    """
    Initialize the logging configuration based on the provided configuration
    dictionary.

    The configuration dictionary should contain a 'logs' key, which itself
    should contain a 'profile' key specifying the desired logging profile.
    If the 'profile' value is 'action', the logging level will be set to INFO.
    Otherwise, the logging level will be set to DEBUG.

    Args:
        config (dict): A dictionary containing the configuration parameters.

    Returns:
        None
    """
    fmt = '[%(asctime)s] %(levelname)-7s %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    if config['logs']['profile'] == 'action':
        logging.basicConfig(level=logging.INFO, format=fmt, datefmt=datefmt)
    else:
        logging.basicConfig(
            level=logging.DEBUG,
            format=fmt,
            datefmt=datefmt)
