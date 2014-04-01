from video_executor import FFMpegExecutor
from system import project_configuration as ProjectConfig

class VideoTools:

    def render_video(self, config):
        #Obtain Environment
        target_folder = ProjectConfig.get('Locations', 'target_folder')
        
        #Obtain Video Conversion Properties
        framerate = ProjectConfig.get('VideoConversion', 'framerate')
        video_codec = ProjectConfig.get('VideoConversion', 'video_codec')
        crf = ProjectConfig.get('VideoConversion', 'crf')
        preset = ProjectConfig.get('VideoConversion', 'preset')
        output_file = ProjectConfig.get('VideoConversion', 'output_file')
        
        #Execute Rendering
        arguments = []
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
