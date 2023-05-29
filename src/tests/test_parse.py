import unittest
import yaml
from unittest.mock import mock_open, patch
from configuration.parse import Yaml


class TestYaml(unittest.TestCase):
    def test_init(self):
        yaml_file = "../config.yaml"
        yaml_data = {'key': 'value'}

        with patch('builtins.open', mock_open(read_data=yaml.dump(yaml_data))):
            yaml_parser = Yaml(yaml_file)

        self.assertEqual(yaml_parser.conf, yaml_data)

    def test_str(self):
        yaml_data = {'key': 'value'}
        yaml_parser = Yaml("../config.yaml")
        yaml_parser._Yaml__conf = yaml_data

        expected_output = str(yaml_data)
        self.assertEqual(str(yaml_parser), expected_output)

    def test_conf(self):
        yaml_data = {'key': 'value'}
        yaml_parser = Yaml("../config.yaml")
        yaml_parser._Yaml__conf = yaml_data

        self.assertEqual(yaml_parser.conf, yaml_data)


if __name__ == '__main__':
    unittest.main()
