#!/usr/bin/env python3
"""
This module generates a pull request description using the OpenAI GPT-3.5 language model.

The module includes a 'main' function that serves as the entry point for the script. It reads configuration from a YAML file,
initializes logging, performs preflight checks, interacts with the GitHub API to retrieve information about the pull request,
generates a diff of the pull request, makes an AI request using the OpenAI model to generate a description based on the diff,
updates the description of the pull request, and sets GitHub Action outputs.

Example usage:
--------------
$ python3 main.py

"""
import os
import sys
import logging

import configuration.logs as logs
import configuration.parse as parse
import configuration.preflight as preflight
import OpenAI.model as model
import GitHub.pullrequest as pr
import GitHub.outputs as outputs

import subprocess

def main():
    """
    The main function that serves as the entry point for the script.

    Returns:
        None
    """
    actionpath = os.environ.get('GITHUB_ACTION_PATH')
    if actionpath:
        yamlfile = f"{actionpath}/config.yaml"
    else:
        yamlfile = 'config.yaml'
    config = parse.Yaml(yamlfile).conf
    logs.init(config)
    env = preflight.Env(config)

    github_token = env.vars['GITHUB_TOKEN']
    pullrequest = pr.PullRequest(github_token)
    logging.info(pullrequest)

    patch = pullrequest.diff()
    logging.debug(patch)

    ai = model.AiRequest(
        env.vars['OPENAI_API_KEY'],
        env.vars['INPUT_TEMPLATE'],
        env.vars['INPUT_TEMPLATE_FILEPATH'],
        env.vars['INPUT_HEADER'],
        env.vars['INPUT_MODEL']
    )
    logging.debug(ai)
    description = ai.generate_description(patch)

    logging.debug(description)
    pullrequest.update_description(description)
    outputs.set_action_outputs({"text": "Success"})


if __name__ == '__main__':
    main()
