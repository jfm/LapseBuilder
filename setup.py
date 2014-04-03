from distutils.core import setup
import sys

sys.path.append('lapsebuilder')
import googlemaps


setup(name='lapsebuilder',
      version='1.0',
      author='Jesper Fussing Mørk',
      author_email='jfm@moerks.dk',
      url='https://github.com/jfm/LapseBuilder/',
      download_url='',
      description='Easy to use Python Application for creating TimeLapse videos using ImageMagick and FFMpeg',
      long_description=LapseBuilder.__doc__,
      package_dir=['lapsebuilder']
      packages=['system', 'video', 'image']
     )
