from __future__ import division
import subprocess
import im_executor

def get_srt_factor(filename):
    width = im_executor.execute_identify(['-format', '%w', filename])
    srt_factor = 1920 / int(width)
    return "{0:.4f}".format(srt_factor)+",0"
