from gi.repository import Gtk, GdkPixbuf
import StringIO


class CropWidget(Gtk.Overlay):
    image = Gtk.Image()

    def __init__(self, *args, **kwargs):
        super(CropWidget, self).__init__(*args, **kwargs)
        self.add(CropWidget.image)

    def set_image(self, image):
        image_buffer = StringIO.StringIO()
        image.save(image_buffer, 'jpeg')
        image_contents = image_buffer.getvalue()
        image_buffer.close()
        image_loader = GdkPixbuf.PixbufLoader()
        image_loader.set_size(750, 450)
        image_loader.write(image_contents)
        resized_image_pixbuf = image_loader.get_pixbuf()
        image_loader.close()

        CropWidget.image.set_from_pixbuf(resized_image_pixbuf)
        CropWidget.image.set_padding(5, 5)
        self.queue_draw()
