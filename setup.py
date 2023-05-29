from setuptools import setup

setup(
    name='openai-pr',
    version='0.0.1',
    author='Antoine Barthelemy',
    description='Pull request descriptions wrote by OpenAI.',
    py_modules=['cli'],
    entry_points={
        'console_scripts': ['openai-pr=cli:main']
    },
)

