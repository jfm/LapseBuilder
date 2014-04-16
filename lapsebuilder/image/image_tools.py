from PIL import Image, ImageEnhance
from image.deflicker import Deflicker


class ImageTools:

    def __init__(self):
        pass

    def manipulate_frame(self, frame, deflicker, resize, **kwargs):
        image = Image.open(frame)
        temp_image = image.copy()

        if deflicker:
            temp_image = self.deflicker(temp_image, kwargs['average_luminance'])

        if resize:
            temp_image = self.resize_image(kwargs['width'], kwargs['height'], temp_image)

        return temp_image

    def manipulate_frames(self, frames, deflicker, resize, **kwargs):
        average_luminance = Deflicker.calculate_average_luminance(frames)

        for index, frame in frames:
            temp_image = self.manipulate_frame(frame, deflicker, resize, kwargs, average_luminance=average_luminance)
            temp_image.save(kwargs['target_folder'] + '/frame_' + ("%05d" % index) + '.jpg')

    def resize_image(self, width, height, temp_image):
        return temp_image.thumbnail((width, height), Image.ANTIALIAS)

    def deflicker(self, temp_image, average_luminance):
        image_luminance = Deflicker.calculate_luminance(temp_image)
        brightness = 1 / (image_luminance / average_luminance)
        enhancer = ImageEnhance.Brightness(temp_image)
        return enhancer.enhance(brightness)
