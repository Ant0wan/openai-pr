import yaml
from yaml.loader import SafeLoader


class Yaml:

    def __init__(self, yamlfile: str):
        with open(yamlfile) as f:
            self.__conf = yaml.load(f, Loader=SafeLoader)

    @property
    def conf(self) -> dict:
        return self.__conf
