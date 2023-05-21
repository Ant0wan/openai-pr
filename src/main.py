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


def main():
    """
    The main function that serves as the entry point for the script.

    Returns:
        None
    """
    # Retrieve the YAML configuration file path
    actionpath = os.environ.get('GITHUB_ACTION_PATH')
    if actionpath:
        yamlfile = f"{actionpath}/config.yaml"
    else:
        yamlfile = 'config.yaml'

    # Parse the YAML configuration
    config = parse.Yaml(yamlfile).conf

    # Initialize logging configuration
    logs.init(config)

    # Perform preflight environment checks
    env = preflight.Env(config)

    # Retrieve the GitHub token
    github_token = env.vars['GITHUB_TOKEN']

    # Create a PullRequest object
    pullrequest = pr.PullRequest(github_token, env)

    # Log the PullRequest object
    logging.debug(pullrequest)

    # Get the diff content for the pull request
    patch = pullrequest.diff()

    # Log the diff content
    logging.debug(patch)

    # Create an AiRequest object for OpenAI
    ai = model.AiRequest(
        env.vars['OPENAI_API_KEY'],
        env.vars['INPUT_TEMPLATE'],
        env.vars['INPUT_TEMPLATE_FILEPATH'],
        env.vars['INPUT_HEADER'],
        env.vars['INPUT_MODEL']
    )

    # Log the AiRequest object
    logging.debug(ai)

    # Generate a description using the diff content
    description = ai.generate_description(patch)

    # Log the generated description
    logging.debug(description)

    # Update the pull request description with the generated description
    pullrequest.update_description(description)

    # Set the action outputs
    outputs.set_action_outputs({"text": "Success"})


if __name__ == '__main__':
    main()
