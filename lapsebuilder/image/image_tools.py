from wand.image import Image


class ImageTools:

    def __init__(self):
        pass

    @staticmethod
    def resize_image(width, height, file_path, index, target_folder):
        target_path = target_folder + '/frame_' + ("%05d" % index) + '.jpg'

        with Image(filename=file_path) as image:
            with image.clone() as image_clone:
                image_clone.transform(resize=str(width) + 'x')
                image_clone.transform(crop=str(width) + 'x' + str(height) + '+0+0')
                image_clone.save(filename=target_path)
