import yaml
from yaml.loader import SafeLoader


# ---
# preflights:
#  env:
#    - GITHUB_TOKEN
#    - GITHUB_TOKEN
#    - FORMAT
#    - MODEL
#    - INTRO_WRAP
#    - INTRO_FMT
# logs:
#  logging: 'configuration/logging.conf'
#  profile: dev  # choose(dev|prod)


class Yaml:

    def __init__(self, yamlfile: str):
        with open(yamlfile) as f:
            self.__conf = yaml.load(f, Loader=SafeLoader)

    @property
    def conf(self) -> dict:
        return self.__conf
