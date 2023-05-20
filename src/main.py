#!/usr/bin/env python3
"""
This module generates a pull request description using
the OpenAI GPT-3.5 language model.
"""
import logging
import os
import sys

import configuration.logs as logs
import configuration.parse as parse
import configuration.preflight as preflight
import OpenAI.model as model
import GitHub.pullrequest as pr
import GitHub.outputs as outputs


def main():
    config = parse.Yaml('config.yaml').conf
    logger = logs.Logger(config)
    env = preflight.Env(config)

    github_token = env.vars['GITHUB_TOKEN']
    pullrequest = pr.PullRequest(github_token)
    logging.info(pullrequest)

    patch = pullrequest.diff()
    logging.debug(patch)

    ai = model.AiRequest(
            env.vars['INPUT_TEMPLATE'],
            env.vars['INPUT_TEMPLATE_FILEPATH'],
            env.vars['INPUT_HEADER'],
            env.vars['INPUT_MODEL']
    )
    logging.debug(ai)
#    description = ai.generate_description(patch)

#    #print(f"text={description}")
#    print(pr.number)
#    description="hey!"
#    gh.change_pull_request_description(pr.number, description)


if __name__ == '__main__':
    main()
