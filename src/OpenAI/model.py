import os
import sys
import openai


class AiRequest:

    def __init__(self, key, template, template_file_path, header, model):
        self.__key = key
        self.__template = self._template(template, template_file_path)
        self.__header = header
        self.__model = model

    def __str__(self):
        return f"Template: {self.__template}, \
Header: {self.__header}, \
Model: {self.__model}"

    @staticmethod
    def _template(template, template_file_path):
        if template:
            return template
        elif template_file_path:
            try:
                # This path need to be absolute using git root dir path +
                # .github/PULL_RE...
                with open(template_file_path, "r") as file:
                    return file.read()
            except FileNotFoundError:
                print("Template file not found.")
                return " "  # should exit fail
            except IOError:
                print("Error reading the file.")
                return " "  # should exit fail

    def generate_description(self, text):
        data = self.__header + self.__template + "\n\n\n" + text
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
        return response.choices[0].text[1::]
