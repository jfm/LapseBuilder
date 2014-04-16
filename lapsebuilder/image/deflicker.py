from PIL import Image, ImageStat
import math


class Deflicker():

    def __init__(self):
        pass

    @staticmethod
    def calculate_luminance(image):
        stat = ImageStat.Stat(image)
        r, g, b = stat.mean
        gs = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

        return gs

    @staticmethod
    def calculate_average_luminance(frames):
        luminance_levels = []
        for frame in frames:
            image = Image.open(frame)
            luminance = Deflicker.calculate_luminance(image)
            luminance_levels.append(luminance)

        return sum(luminance_levels)/len(frames)

