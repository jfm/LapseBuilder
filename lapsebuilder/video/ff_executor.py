import subprocess

def execute_ffmpeg(arguments):
    #argument_string = ' '.join(str(argument) for argument in arguments)
    #print "Running with ffmpeg arguments: " + argument_string
    arguments.insert(0, "ffmpeg")
    return subprocess.check_output(arguments)