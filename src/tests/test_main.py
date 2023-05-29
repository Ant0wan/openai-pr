import unittest
from unittest.mock import patch, MagicMock
import os
import logging
from main import main


class TestMain(unittest.TestCase):
    @patch('main.parse.Yaml')
    @patch('main.logs.init')
    @patch('main.preflight.Env')
    @patch('main.pr.PullRequest')
    @patch('main.model.AiRequest')
    @patch('main.outputs.set_action_outputs')
    def test_main(self, mock_set_action_outputs, mock_AiRequest,
                  mock_PullRequest, mock_Env, mock_init, mock_Yaml):
        # Mock the necessary objects
        mock_Yaml.return_value.conf = {}
        mock_Env.return_value.vars = {'GITHUB_TOKEN': 'dummy_token'}
        mock_PullRequest_instance = mock_PullRequest.return_value
        mock_PullRequest_instance.diff.return_value = 'dummy_diff_content'
        mock_AiRequest_instance = mock_AiRequest.return_value
        mock_AiRequest_instance.generate_description.return_value = 'dummy_description'

        # Mock the environment variable
        with patch.dict(os.environ, {'GITHUB_ACTION_PATH': '/dummy/path'}):
            main()

        # Assert the function calls
        mock_Yaml.assert_called_once_with('/dummy/path/config.yaml')
        mock_init.assert_called_once_with({})
        mock_PullRequest.assert_called_once_with(
            'dummy_token', mock_Env.return_value)
        mock_PullRequest_instance.diff.assert_called_once()
        mock_AiRequest.assert_called_once_with(mock_Env.return_value)
        mock_AiRequest_instance.generate_description.assert_called_once_with(
            'dummy_diff_content')
        mock_PullRequest_instance.update_description.assert_called_once_with(
            'dummy_description')
        mock_set_action_outputs.assert_called_once_with({"text": "Success"})


if __name__ == '__main__':
    unittest.main()
