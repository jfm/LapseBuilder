import ff_executor

def render_video(config):
    #Obtain Environment
    target_folder = config.get('Locations', 'target_folder')
    
    #Obtain Video Conversion Properties
    framerate = config.get('VideoConversion', 'framerate')
    video_codec = config.get('VideoConversion', 'video_codec')
    crf = config.get('VideoConversion', 'crf')
    preset = config.get('VideoConversion', 'preset')
    
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
    arguments.append(target_folder + '/timelapse.mkv')
    
    ff_executor.execute_ffmpeg(arguments)
