from video_executor import FFMpegExecutor
from system import project_configuration as project_config


class VideoTools:

    def __init__(self):
        pass

    @staticmethod
    def render_video():
        #Obtain Environment
        target_folder = project_config.get('Locations', 'target_folder')
        
        #Obtain Video Conversion Properties
        framerate = project_config.get('VideoConversion', 'framerate')
        video_codec = project_config.get('VideoConversion', 'video_codec')
        crf = project_config.get('VideoConversion', 'crf')
        preset = project_config.get('VideoConversion', 'preset')
        output_file = project_config.get('VideoConversion', 'output_file')
        
        #Execute Rendering
        arguments = list()
        arguments.append('-pattern_type')
        arguments.append('glob')
        arguments.append('-i')
        arguments.append(target_folder + '/*.jpg')
        arguments.append('-r')
        arguments.append(framerate)
        arguments.append('-y')
        arguments.append('-vcodec')
        arguments.append(video_codec)
        arguments.append('-crf')
        arguments.append(crf)
        arguments.append('-preset')
        arguments.append(preset)
        arguments.append(target_folder + '/' + output_file)
        
        executor = FFMpegExecutor()
        executor.execute(arguments)
