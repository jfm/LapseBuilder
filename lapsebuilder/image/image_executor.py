import subprocess


class IMExecutor:

    def __init__(self):
        pass

    @staticmethod
    def execute_convert(arguments):
        #argument_string = ' '.join(str(argument) for argument in arguments)
        #print "Running with convert arguments: " + argument_string
        arguments.insert(0, "convert")
        return subprocess.check_output(arguments)

    @staticmethod
    def execute_identify(arguments):
        #argument_string = ' '.join(str(argument) for argument in arguments)
        #print "Running with identify arguments: " + argument_string
        arguments.insert(0, "identify")
        return subprocess.check_output(arguments)