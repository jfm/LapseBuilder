import unittest
from wand.image import Image

from image.image_tools import ImageTools

class test_image_tools(unittest.TestCase):

    def test_resize_image(self):
        image_tools = ImageTools()
        file_path = './test/resources/org_image.jpg'
        result_folder = './test/resources/results'
        image_tools.resize_image(1920, 1080, file_path, 0, result_folder)

        #Test width is now 1920
        result_width = self.get_image_width('./test/resources/results/frame_00000.jpg')
        self.assertEqual(1920, result_width)

        #Test height is now 1080
        result_height = self.get_image_height('./test/resources/results/frame_00000.jpg')
        self.assertEqual(1080, result_height)
        
    def get_image_height(self, file_path):
        with Image(filename=file_path) as result_image:
            return result_image.height
            
    def get_image_width(self, file_path):
        with Image(filename=file_path) as result_image:
            return result_image.width

if __name__ == "__main__":
    unittest.main()