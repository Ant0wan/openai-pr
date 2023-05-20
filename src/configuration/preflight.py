import os
import logging


class Env:

    def __init__(self, config: dict):
        self.__vars = self._preflight_checks(
            config['preflights']['env'])
        logging.debug(self.__vars)

    @staticmethod
    def _preflight_checks(var_names: list) -> dict:
        """Check all needed environment variables
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
        return self.__vars
