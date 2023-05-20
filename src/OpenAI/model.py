import os
import sys
import openai


class AiRequest:

    def __init__(self, template, template_file_path, header, model):
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
            except IOError:
                print("Error reading the file.")

# Ability to specify, path to PULL_REQUEST_TEMPLATE
# A default format
# or None
# Should retreive info from .github/PULL_REQUEST_TEMPLATE.md if format not
# specified

#    template_content = os.getenv('INPUT_TEMPLATE_CONTENT')
#    template_filepath = os.getenv('INPUT_TEMPLATE_FILEPATH')
#    if template_content and template_filepath:
#        exit('ERROR: cannot specify both template and filepath')
#    elif template_content:
#        template = template_content
#    elif template_filepath:
#        with open(template_filepath, 'r') as file:
#            template = file.read()
#    else:
#        exit('ERROR: specify either template or filepath')


def generate_pull_request_description(stdin):
    data = INTRO_WRAP + stdin + INTRO_FMT + FORMAT
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model=MODEL,
        prompt=data,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    return response.choices[0].text[1::]
