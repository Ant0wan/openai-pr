"""
This module provides functions for setting outputs in GitHub Actions or logging to the terminal in CLI mode.

The module includes a function, 'set_action_outputs', that sets the GitHub Action outputs if running as a
GitHub Action. If running in CLI mode, the function logs the outputs to the terminal. Note that if the CLI
mode is used within a GitHub Actions workflow, it will be treated the same as GitHub Actions mode.

Example usage:
--------------
output_pairs = {
    'output_key1': 'output_value1',
    'output_key2': 'output_value2'
}

set_action_outputs(output_pairs)

"""
import os
import logging


def set_action_outputs(output_pairs):
    """
    Sets the GitHub Action outputs if running as a GitHub Action,
    and otherwise logs these to the terminal if running in CLI mode. Note
    that if the CLI mode is used within a GitHub Actions
    workflow, it will be treated the same as GitHub Actions mode.

    Args:
        output_pairs (dict): Dictionary of outputs with values.

    Returns:
        None
    """
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            for key, value in output_pairs.items():
                print("{0}={1}".format(key, value), file=f)
    else:
        for key, value in output_pairs.items():
            print("{0}={1}".format(key, value))
