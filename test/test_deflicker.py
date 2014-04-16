import unittest
#from wand.image import Image
from image.deflicker import Deflicker
from system.system_tools import FileTools

class test_image_tools(unittest.TestCase):

    def test_calculate_average_luminance(self):
        deflicker = Deflicker()
        frames = FileTools.get_source_file_list('./test/resources/')
        print deflicker.calculate_average_luminance(frames)

if __name__ == "__main__":
    unittest.main()