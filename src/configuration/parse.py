"""
This module provides a YAML file parser class.

The module includes a class, 'Yaml', that can be used to load and
parse a YAML file. The YAML file is loaded using the PyYAML library and
the 'SafeLoader' loader. The parsed YAML data can be accessed through
the 'conf' property of the 'Yaml' class.

Example usage:
--------------
yaml_file = "config.yaml"
yaml_parser = Yaml(yaml_file)
data = yaml_parser.conf

"""
import yaml
from yaml.loader import SafeLoader


class Yaml:
    """
    A YAML file parser class.

    The 'Yaml' class can be used to load and parse a YAML file.
    The parsed YAML data can be accessed through the 'conf' property.

    Example usage:
    --------------
    yaml_file = "config.yaml"
    yaml_parser = Yaml(yaml_file)
    data = yaml_parser.conf
    """

    def __init__(self, yamlfile: str):
        """
        Initialize the YAML parser with the provided YAML file.

        The YAML file is loaded using the PyYAML library and
        the 'SafeLoader' loader.

        Args:
            yamlfile (str): The path to the YAML file.

        Returns:
            None
        """
        with open(yamlfile, "r", encoding="utf-8") as file:
            self.__conf = yaml.load(file, Loader=SafeLoader)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string representation of the object, formatted as "{conf}".
        """
        return f"{self.__conf}"

    @property
    def conf(self) -> dict:
        """
        Get the parsed YAML data as a dictionary.

        Returns:
            dict: The parsed YAML data.
        """
        return self.__conf
