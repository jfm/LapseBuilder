import subprocess

class IMExecutor:

    def execute_convert(self, arguments):
        #argument_string = ' '.join(str(argument) for argument in arguments)
        #print "Running with convert arguments: " + argument_string
        arguments.insert(0, "convert")
        return subprocess.check_output(arguments)
        
    def execute_identify(self, arguments):
        #argument_string = ' '.join(str(argument) for argument in arguments)
        #print "Running with identify arguments: " + argument_string
        arguments.insert(0, "identify")
        return subprocess.check_output(arguments)