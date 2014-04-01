import sys
sys.path.append("lapsebuilder")

from system.system_tools import FileTools
from  system import project_configuration as ProjectConfig
from image.image_tools import ImageTools
from video.video_tools import VideoTools

def convert_images(filenames):
    image_tools = ImageTools()
    
    for index, filename in enumerate(filenames):
        image_tools.resize_image(filename, index)

def render_video():
    video_tools = VideoTools()
    
    video_tools.render_video()
        
if  __name__ =='__main__':
    cmd_arguments = str(sys.argv)

    if len(sys.argv) < 2:
        print 'You need to specify a project file'
        exit(1)
    else:
        #Initialize the project Configuration
        ProjectConfig.initialize(str(sys.argv[1]))

        #Obtain List of Source Files
        file_tools = FileTools()
        source_folder = ProjectConfig.get("Locations", "source_folder")
        source_files = file_tools.get_source_file_list(source_folder)

        #Convert and Resize Images to specified resolution
        convert_images(source_files)
        
        #Render Video
        render_video(config)


