import yaml
import sys
import object.object

def quote(string, char='\''):
    return char + str(string) + char


def str_to_class(s):
    return getattr(sys.modules['object.object'], s)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class config:
    def __init__(self, file):
        self.file = file

    def import_settings(self):

        with open(self.file, "r") as ymlfile:
            cfg = yaml.safe_load(ymlfile)

        self.all = cfg

        self.database_name = cfg['database']['database_name']
        self.user = cfg['database']['user']
        self.password = cfg['database']['password']
        self.host = cfg['database']['host']
        self.port = cfg['database']['port']
        self.schemas = cfg['database']['schemas']