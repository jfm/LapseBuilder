from image_executor import IMExecutor
from image_utils import IMUtils
from system import project_configuration as ProjectConfig

class ImageTools:

    def resize_image(self, filename, index):
        #Obtain Environment
        source_folder = ProjectConfig.get('Locations', 'source_folder')
        target_folder = ProjectConfig.get('Locations', 'target_folder')
        
        #Obtain Image Conversion Properties
        gravity = ProjectConfig.get('ImageConversion', 'gravity')
        resolution = ProjectConfig.get('ImageConversion', 'resolution')
        crop_offset = ProjectConfig.get('ImageConversion', 'crop_offset')
        
        #Calculate SRT factor
        utils = IMUtils()
        srt_factor_string = utils.get_srt_factor(source_folder + '/' + filename)
        
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

        executor = IMExecutor()
        executor.execute_convert(arguments)
