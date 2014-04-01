import ConfigParser

configuration = ConfigParser.ConfigParser()

def initialize(project_filename):
    configuration.read(project_filename)
    
def get(section, property):
    return configuration.get(section, property)