import os
import unittest
from unittest.mock import patch
from ghkit.outputs import set_action_outputs


class TestSetActionOutputs(unittest.TestCase):
    def test_set_action_outputs_in_cli_mode(self):
        output_pairs = {
            'output_key1': 'output_value1',
            'output_key2': 'output_value2'
        }

        with patch('builtins.print') as mock_print:
            set_action_outputs(output_pairs)

            # Verify that the outputs are printed to the terminal
            expected_calls = [
                unittest.mock.call('output_key1=output_value1'),
                unittest.mock.call('output_key2=output_value2'),
            ]
            mock_print.assert_has_calls(expected_calls, any_order=True)


if __name__ == '__main__':
    unittest.main()
