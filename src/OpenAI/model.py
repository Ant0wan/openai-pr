"""
This file contains the AiRequest class, which represents an AI request for generating a description
based on input text.

It utilizes the OpenAI library to interact with the OpenAI service and performs text generation
using a provided template.

Author: Antoine Barthelemy <antoine@linux.com>

Date: 2023-05-21
"""

import openai


class AiRequest:
    """
    Represents an AI request for generating a description based on input text.

    Args:
        env (object): The environment object containing the necessary variables.

    Attributes:
        __key (str): The API key for the OpenAI service.
        __template (str): The template text used for generating descriptions.
        __header (str): The header text appended to the template.
        __model (str): The model used for generating descriptions.

    Methods:
        __init__(self, env): Initializes the AiRequest object.
        __str__(self): Returns a string representation of the AiRequest object.
        _template(template, template_file_path): Retrieves the template text.
        generate_description(text): Generates a description based on the provided text.
    """

    def __init__(self, env):
        """
        Initializes the AiRequest object.

        Args:
            env (object): The environment object containing the necessary variables.
        """
        self.__key = env.vars['OPENAI_API_KEY']
        self.__template = self._template(
            env.vars['INPUT_TEMPLATE'],
            env.vars['INPUT_TEMPLATE_FILEPATH'])
        self.__header = env.vars['INPUT_HEADER']
        self.__model = env.vars['INPUT_MODEL']

    def __str__(self):
        """
        Returns a string representation of the AiRequest object.

        Returns:
            str: A string representation of the AiRequest object.
        """
        return f"Template: {self.__template}, Header: {self.__header}, Model: {self.__model}"

    @staticmethod
    def _template(template, template_file_path):
        """
        Retrieves the template text either from the provided template or from a template file.

        Args:
            template (str): The template text.
            template_file_path (str): The file path of the template file.

        Returns:
            str: The template text.

        Raises:
            FileNotFoundError: If the template file is not found.
            IOError: If there is an error reading the file.
        """
        if template:
            return template
        try:
            with open(template_file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError as file_not_found_error:
            raise FileNotFoundError(
                "Template file not found.") from file_not_found_error
        except IOError as io_error:
            raise IOError("Error reading the file.") from io_error

    def generate_description(self, text):
        """
        Generates a description based on the provided text.

        Args:
            text (str): The input text for generating the description.

        Returns:
            str: The generated description.

        Raises:
            openai.error.OpenAIError: If there is an error in the AI request.
        """
        data = self.__header + self.__template + "\n\n" + text
        openai.api_key = self.__key
        response = openai.Completion.create(
            model=self.__model,
            prompt=data,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        return response.choices[0].text
