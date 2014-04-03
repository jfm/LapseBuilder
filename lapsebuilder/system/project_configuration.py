import ConfigParser

configuration = ConfigParser.ConfigParser()


def initialize(project_filename):
    configuration.read(project_filename)


def get(section, config_property):
    return configuration.get(section, config_property)