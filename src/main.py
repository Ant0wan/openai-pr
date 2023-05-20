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


def set_action_outputs(output_pairs):
    """Sets the GitHub Action outputs if running as a GitHub Action,
    and otherwise logs these to terminal if running in CLI mode. Note
    that if the CLI mode is used within a GitHub Actions
    workflow, it will be treated the same as GitHub Actions mode.

    Keyword arguments:
    output_pairs - Dictionary of outputs with values
    """
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            for key, value in output_pairs.items():
                print("{0}={1}".format(key, value), file=f)
    else:
        for key, value in output_pairs.items():
            print("{0}={1}".format(key, value))


def main():
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
    print(gh.get_pull_request_diff())
#    input_str = "key hey key"
#    output = model.generate_pull_request_description(input_str)
#    set_action_outputs({"text": output})
#    print(f"text={output}")
# - name: Save state
# run: echo "{name}={value}" >> $GITHUB_STATE
# - name: Set output
# run: echo "text={value}" >> $GITHUB_OUTPUT
#

#    access_token = "your_access_token_here"
#    gh.print_user_repos(access_token)


if __name__ == '__main__':
    main()
