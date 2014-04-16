from gi.repository import Gtk
from ui.crop_widget import CropWidget
from image.image_tools import ImageTools


class ImageFrame(Gtk.Frame):
    crop_widget = CropWidget()

    def __init__(self, *args, **kwargs):
        super(ImageFrame, self).__init__(*args, **kwargs)

        widget_grid = Gtk.Grid()
        widget_grid.set_row_spacing(5)
        widget_grid.set_column_spacing(5)
        widget_grid.props.valign = Gtk.Align.CENTER
        widget_grid.props.halign = Gtk.Align.CENTER
        widget_grid.add(ImageFrame.crop_widget)

        self.add(widget_grid)

    @staticmethod
    def load_image(file_path):
        image = ImageTools.manipulate_frame(file_path, False, False)
        ImageFrame.crop_widget.set_image(image)
