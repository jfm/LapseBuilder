import subprocess


class FFMpegExecutor:

    def __init__(self):
        pass

    @staticmethod
    def execute(arguments):
        arguments.insert(0, "ffmpeg")
        return subprocess.check_output(arguments)