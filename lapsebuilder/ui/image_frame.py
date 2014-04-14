from gi.repository import Gtk


class ImageFrame(Gtk.Frame):

    def __init__(self, *args, **kwargs):
        super(ImageFrame, self).__init__(*args, **kwargs)

        #widget_grid = Gtk.Grid()
        #widget_grid.set_row_spacing(5)
        #widget_grid.set_column_spacing(5)

        test_label = Gtk.Label('IMAGE_FRAME_LABEL')
        self.add(test_label)
