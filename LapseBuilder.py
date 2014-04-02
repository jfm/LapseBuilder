import sys
sys.path.append("lapsebuilder")

from system.system_tools import FileTools
from  system import project_configuration as ProjectConfig
from image.image_tools import ImageTools
from video.video_tools import VideoTools

def convert_images(filenames):
    image_tools = ImageTools()
    
    #Obtain Environment
    source_folder = ProjectConfig.get('Locations', 'source_folder')
    target_folder = ProjectConfig.get('Locations', 'target_folder')

    #Obtain Target Resolution
    target_width = ProjectConfig.get('ImageConversion', 'resolution_width')
    target_height = ProjectConfig.get('ImageConversion', 'resolution_height')
    
    for index, filename in enumerate(filenames):
        file_path = source_folder + '/' + filename
        image_tools.resize_image(target_width, target_height, file_path, index, target_folder)

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
        render_video()


