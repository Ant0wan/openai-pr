import os
import sys
import openai


INTRO_WRAP = "Based on the output of the command `git diff`, \
could you please generate a pull request description using the \
provided information? Be concise.\n"
INTRO_FMT = "Description must follow this format:\n"

# Ability to specify, path to PULL_REQUEST_TEMPLATE
# A default format
# or None
# Should retreive info from .github/PULL_REQUEST_TEMPLATE.md if format not
# specified
MODEL = "text-davinci-003"  # In github action default
FORMAT = ""


def generate_pull_request_description(stdin):
    """
    Generate a pull request description based on the provided input.

    Args:
     stdin (str): The input string for generating the pull request description.

    Returns:
     str: The generated pull request description.
    """
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
