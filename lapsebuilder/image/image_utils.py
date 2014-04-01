from __future__ import division
import subprocess

from image_executor import IMExecutor

class IMUtils:

    def get_srt_factor(self, filename):
        executor = IMExecutor()

        #Width Arguments
        arguments = []
        arguments.append('-format')
        arguments.append('%w')
        arguments.append(filename)

        #Execute identify to obtain width of image
        width = executor.execute_identify(arguments)
        srt_factor = 1920 / int(width)
        
        return "{0:.4f}".format(srt_factor)+",0"
