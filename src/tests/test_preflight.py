"""
Unit tests for the Env class in the configuration.preflight module.
"""

import unittest
from unittest.mock import patch
from configuration.preflight import Env


class TestEnv(unittest.TestCase):
    """Test case for the Env class."""

    def test_init(self):
        """Test the initialization of Env class."""
        config = {
            'preflights': {
                'env': ['ENV_VAR_1', 'ENV_VAR_2']
            }
        }
        env_vars = {'ENV_VAR_1': 'value1', 'ENV_VAR_2': 'value2'}

        with patch('os.environ', env_vars):
            env_loader = Env(config)

        self.assertEqual(env_loader.vars, env_vars)

    def test_str(self):
        """Test the string representation of Env class."""
        env_vars = {'ENV_VAR_1': 'value1', 'ENV_VAR_2': 'value2'}
        env_loader = Env({
            'preflights': {
                'env': ['ENV_VAR_1', 'ENV_VAR_2']
            }
        })
        env_loader._Env__vars = env_vars

        expected_output = str(env_vars)
        self.assertEqual(str(env_loader), expected_output)

    def test_vars(self):
        """Test the vars property of Env class."""
        env_vars = {'ENV_VAR_1': 'value1', 'ENV_VAR_2': 'value2'}
        env_loader = Env({
            'preflights': {
                'env': ['ENV_VAR_1', 'ENV_VAR_2']
            }
        })
        env_loader._Env__vars = env_vars

        self.assertEqual(env_loader.vars, env_vars)


if __name__ == '__main__':
    unittest.main()
