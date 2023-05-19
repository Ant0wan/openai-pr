#!/usr/bin/env python3
"""
This module generates a pull request description using
the OpenAI GPT-3.5 language model.
"""
import os
import sys

import configuration.logger as logger
import configuration.parser as parser
import configuration.preflights as preflights
import ai.model as model
import gh.gh as gh


def main():
    template_content = os.getenv('INPUT_TEMPLATE_CONTENT')
    template_filepath = os.getenv('INPUT_TEMPLATE_FILEPATH')
    if template_content and template_filepath:
        exit('ERROR: cannot specify both template and filepath')
    elif template_content:
        template = template_content
    elif template_filepath:
        with open(template_filepath, 'r') as file:
            template = file.read()
    else:
        exit('ERROR: specify either template or filepath')
    input_str = sys.stdin.read()
    output = model.generate_pull_request_description(input_str)
    print(output)
#    access_token = "your_access_token_here"
#    gh.print_user_repos(access_token)


if __name__ == '__main__':
    main()
