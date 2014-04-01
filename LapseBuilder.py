import sys
import ConfigParser

sys.path.append("lapsebuilder")

from im import tools
from system import file_tools
from video import ffmpeg

def convert_images(config, filenames):
    for index, filename in enumerate(filenames):
        tools.resize_image(config, filename, index)

def render_video(config):
    ffmpeg.render_video(config)
        
def main(config):
    source_folder = config.get("Locations", "source_folder")
    source_files = file_tools.get_source_file_list(source_folder)

    #Convert and Resize Images to specified resolution
    convert_images(config, source_files)

    #Render Video
    render_video(config)

if  __name__ =='__main__':
    cmd_arguments = str(sys.argv)

    if len(sys.argv) < 2:
        print 'You need to specify a project file'
        exit(1)
    else:
        config = ConfigParser.ConfigParser()
        config.read(str(sys.argv[1]))
        main(config)


