import unittest
import logging
from configuration.logs import init

class TestLogs(unittest.TestCase):
    def test_init_action_profile(self):
        config = {
            'logs': {
                'profile': 'action'
            }
        }
        init(config)
        self.assertEqual(logging.getLogger().getEffectiveLevel(), logging.INFO)

    def test_init_debug_profile(self):
        config = {
            'logs': {
                'profile': 'debug'
            }
        }
        init(config)
        self.assertEqual(logging.getLogger().getEffectiveLevel(), logging.DEBUG)

if __name__ == '__main__':
    unittest.main()

