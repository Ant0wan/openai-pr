import os
import sys
import openai

class AiRequest:

    header = "Based on the output of the command `git diff`, could you please generate a pull request description using the provided information? Be concise.\nDescription must follow this format:\n"
    template_file_path = ".github/PULL_REQUEST_TEMPLATE.md"

    def __init__(self, template="", template_file_path=AiRequest.template_path, header=AiRequest.header, model="text-davinci-003"):
        self.__header = header
        self.__model = model
        self.__template = template


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
