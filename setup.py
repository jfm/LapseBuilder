from distutils.core import setup
import sys

sys.path.append('lapsebuilder')

setup(name='lapsebuilder',
      version='0.1',
      author='Jesper Fussing Moerk',
      author_email='jfm@moerks.dk',
      url='https://github.com/jfm/LapseBuilder/',
      download_url='',
      description='Easy to use Python Application for creating TimeLapse videos using ImageMagick and FFMpeg',
      long_description='Hello World',
      packages=['lapsebuilder', 'lapsebuilder.system', 'lapsebuilder.video', 'lapsebuilder.image'],
      py_modules=['LapseBuilder'])
