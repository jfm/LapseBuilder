import im_executor
import helpers

def resize_image(config, filename, index):
    #Obtain Environment
    source_folder = config.get('Locations', 'source_folder')
    target_folder = config.get('Locations', 'target_folder')
    
    #Obtain Image Conversion Properties
    gravity = config.get('ImageConversion', 'gravity')
    resolution = config.get('ImageConversion', 'resolution')
    crop_offset = config.get('ImageConversion', 'crop_offset')

    #Calculate SRT factor
    srt_factor_string = helpers.get_srt_factor(source_folder + '/' + filename)

    #Result Filename
    result_file = 'frame_' + ("%05d" % index) + '.jpg'
    
    #Execute Resize Conversion
    arguments = []
    arguments.append(source_folder + '/' + filename)
    arguments.append('-distort')
    arguments.append('SRT')
    arguments.append(srt_factor_string)
    arguments.append('-gravity')
    arguments.append(gravity)
    arguments.append('-crop')
    arguments.append(resolution+''+crop_offset)
    arguments.append('+repage')
    arguments.append(target_folder + '/' + result_file)
    im_executor.execute_convert(arguments)
