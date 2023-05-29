import unittest
from unittest.mock import patch, Mock
from opnai.model import AiRequest
from configuration.preflight import Env


class AiRequestTestCase(unittest.TestCase):
    @patch('openai.Completion.create')
    def test_generate_description(self, mock_create):
        mock_create.return_value = Mock(
            choices=[Mock(text='Generated description')])

        env_vars = {
            'OPENAI_API_KEY': 'mock-api-key',
            'INPUT_TEMPLATE': 'mock-template',
            'INPUT_TEMPLATE_FILEPATH': 'mock-template-filepath',
            'INPUT_HEADER': 'mock-header',
            'INPUT_MODEL': 'mock-model'
        }
        with patch.dict('os.environ', env_vars):
            env_loader = Env({'preflights': {'env': list(env_vars.keys())}})
            ai_request = AiRequest(env_loader)

            text = 'Input text'
            description = ai_request.generate_description(text)

            mock_create.assert_called_once_with(
                model='mock-model',
                prompt='mock-headermock-template\n\nInput text',
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
            )
            self.assertEqual(description, 'Generated description')


if __name__ == '__main__':
    unittest.main()
