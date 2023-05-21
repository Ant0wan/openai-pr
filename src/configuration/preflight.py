"""
This file contains the Env class, which is an environment variable loader.

The Env class is used to load and check environment variables based
on a provided configuration.
The loaded environment variables can be accessed through the 'vars' property.

Example usage:
--------------
config = {
    'preflights': {
        'env': ['ENV_VAR_1', 'ENV_VAR_2']
    }
}

env_loader = Env(config)
variables = env_loader.vars
"""

import os
import logging


class Env:
    """
    An environment variable loader class.

    The 'Env' class can be used to load and check environment variables based
    on a provided configuration. The loaded environment variables can be
    accessed through the 'vars' property.

    Args:
        config (dict): A dictionary containing the configuration parameters.

    Attributes:
        __vars (dict): A dictionary containing the loaded env variables.

    Methods:
        __init__(self, config): Initialize the environment variable loader with
                                the provided configuration.
        _preflight_checks(var_names): Perform preflight checks to ensure that
                            all specified environment variables are present.
        vars: Get the loaded environment variables as a dictionary.
    """

    def __init__(self, config: dict):
        """
        Initialize the environment variable loader with
        the provided configuration.

        The configuration dictionary should contain a 'preflights' key, which
        itself should contain an 'env' key specifying the required environment
        variables. The 'Env' class performs preflight checks to ensure that all
        the specified environment variables are present.

        Args:
            config (dict): A dictionary containing configuration parameters.

        Returns:
            None
        """
        self.__vars = self._preflight_checks(
            config['preflights']['env'])
        logging.debug(self.__vars)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string representation of the object, formatted as "{vars}".
        """
        return f"{self.__vars}"

    @staticmethod
    def _preflight_checks(var_names: list) -> dict:
        """
        Perform preflight checks to ensure that all the specified
        environment variables are present.

        Args:
            var_names (list): A list of environment variable names.

        Returns:
            dict: A dictionary containing the loaded environment variables.

        Raises:
            KeyError: If any of the required environment variables is missing.
        """
        env_variables = {}
        for var in var_names:
            try:
                env_variables[var] = os.environ[var]
            except KeyError:
                logging.error("%s variable missing!", var)
                os._exit(os.EX_CONFIG)
        return env_variables

    @property
    def vars(self):
        """
        Get the loaded environment variables as a dictionary.

        Returns:
            dict: The loaded environment variables.
        """
        return self.__vars
