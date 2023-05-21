"""
This module provides a class for making AI requests using OpenAI.

The module includes a class, 'AiRequest', that can be used to make AI requests using OpenAI.
The 'AiRequest' class requires a key for authentication, a template or a template file path,
a header, and a model. It provides a method for generating descriptions based on the provided text.

Example usage:
--------------
key = "your_openai_key"
template = "Your template text"
template_file_path = "path_to_template_file.txt"
header = "Your header text"
model = "your_model_name"

ai_request = AiRequest(key, template, template_file_path, header, model)

# Generate description
text = "Your text"
description = ai_request.generate_description(text)

# Print information about the AI request
print(ai_request)

"""
import os
import sys
import openai
import logging


class AiRequest:
    """
    A class for making AI requests using OpenAI.

    The 'AiRequest' class requires a key for authentication, a template or a template file path,
    a header, and a model.
    It provides a method for generating descriptions based on the provided text.

    Example usage:
    --------------
    key = "your_openai_key"
    template = "Your template text"
    template_file_path = "path_to_template_file.txt"
    header = "Your header text"
    model = "your_model_name"

    ai_request = AiRequest(key, template, template_file_path, header, model)

    # Generate description
    text = "Your text"
    description = ai_request.generate_description(text)

    # Print information about the AI request
    print(ai_request)
    """

    def __init__(self, key, template, template_file_path, header, model):
        """
        Initialize the AiRequest object with the provided key, template,
        template file path, header, and model.

        Args:
            key (str): The OpenAI key for authentication.
            template (str): The template text.
            template_file_path (str): The file path of the template file.
            header (str): The header text.
            model (str): The name of the AI model.

        Returns:
            None
        """
        self.__key = key
        self.__template = self._template(template, template_file_path)
        self.__header = header
        self.__model = model

    def __str__(self):
        """
        Return a string representation of the AiRequest object.

        Returns:
            str: A string representation of the AiRequest object.
        """
        return f"Template: {self.__template}, \
Header: {self.__header}, \
Model: {self.__model}"

    @staticmethod
    def _template(template, template_file_path):
        """
        Get the template text either from the provided template or from a template file.

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
        elif template_file_path:
            try:
                with open(template_file_path, "r") as file:
                    return file.read()
            except FileNotFoundError:
                raise FileNotFoundError("Template file not found.")
            except IOError:
                raise IOError("Error reading the file.")

    def generate_description(self, text):
        """
        Generate a description based on the provided text.

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
