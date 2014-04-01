import unittest

from system import file_tools

class test_file_tools(unittest.TestCase):

    def test_get_source_file_list(self):
        result_list = ['file_0001.jpg', 'file_0002.jpg', 'file_0003.jpg', 'file_0004.jpg', 'file_0005.jpg']
        source_list = file_tools.get_source_file_list('./test/resources/')
        self.assertEqual(source_list, result_list)

if __name__ == "__main__":
    unittest.main()