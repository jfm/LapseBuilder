from gi.repository import Gtk, GdkPixbuf


class CropWidget(Gtk.Overlay):
    image = Gtk.Image()

    def __init__(self, *args, **kwargs):
        super(CropWidget, self).__init__(*args, **kwargs)
        self.add(CropWidget.image)

    def set_image(self, file_path):
        resized_image_pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_scale(file_path, 750, 500, True)
        CropWidget.image.set_from_pixbuf(resized_image_pixbuf)
        CropWidget.image.set_padding(5, 5)
        self.queue_draw()

    #WIDTH: 750, HEIGHT: 421
    def add_crop_box(self, pixel_width, pixel_height):
        box = Gtk.DrawingArea()

        pass