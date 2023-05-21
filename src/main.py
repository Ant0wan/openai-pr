#!/usr/bin/env python3
"""
This module generates a pull request description using the OpenAI GPT-3.5
language model.

The module includes a 'main' function that serves as the entry point for
the script. It reads configuration from a YAML file, initializes logging,
performs preflight checks, interacts with the GitHub API to retrieve
information about the pull request, generates a diff of the pull request,
makes an AI request using the OpenAI model to generate a description
based on the diff, updates the description of the pull request,
and sets GitHub Action outputs.

Example usage:
--------------
$ python3 main.py

"""

import os
import logging

from configuration import logs
from configuration import parse
from configuration import preflight

from OpenAI import model

from ghkit import outputs
import ghkit.pullrequest as pr


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
    logging.info(pullrequest)

    # Get the diff content for the pull request
    patch = pullrequest.diff()

    # Log the diff content
    logging.info(patch)

    # Create an AiRequest object for OpenAI
    air = model.AiRequest(env)

    # Log the AiRequest object
    logging.debug(air)

    # Generate a description using the diff content
    description = air.generate_description(patch)

    # Log the generated description
    logging.debug(description)

    # Update the pull request description with the generated description
    pullrequest.update_description(description)

    # Set the action outputs
    outputs.set_action_outputs({"text": "Success"})


if __name__ == '__main__':
    main()
