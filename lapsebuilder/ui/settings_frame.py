from gi.repository import Gtk


class SettingsFrame(Gtk.Frame):

    def __init__(self, *args, **kwargs):
        super(SettingsFrame, self).__init__(*args, **kwargs)

        widget_grid = Gtk.Grid()
        widget_grid.set_row_spacing(5)
        widget_grid.set_column_spacing(5)

        #Source Folder
        source_label = Gtk.Label('Source Folder')
        source_label.set_alignment(0.02, 0.5)
        widget_grid.attach(source_label, 1, 1, 2, 1)
        source_folder_entry = Gtk.Entry()
        widget_grid.attach_next_to(source_folder_entry, source_label, Gtk.PositionType.BOTTOM, 1, 1)
        source_folder_button = Gtk.Button("Browse")
        source_folder_button.connect("clicked", self.on_source_folder_button_clicked)
        widget_grid.attach_next_to(source_folder_button, source_folder_entry, Gtk.PositionType.RIGHT, 1, 1)

        #Target Folder
        target_label = Gtk.Label('Target Folder')
        target_label.set_alignment(0.02, 0.5)
        widget_grid.attach(target_label, 1, 3, 2, 1)
        target_folder_entry = Gtk.Entry()
        widget_grid.attach_next_to(target_folder_entry, target_label, Gtk.PositionType.BOTTOM, 1, 1)
        target_folder_button = Gtk.Button("Browse")
        target_folder_button.connect("clicked", self.on_target_folder_button_clicked)
        widget_grid.attach_next_to(target_folder_button, target_folder_entry, Gtk.PositionType.RIGHT, 1, 1)

        #Target Movie File
        file_label = Gtk.Label('Target Filename')
        file_label.set_alignment(0.02, 0.5)
        widget_grid.attach_next_to(file_label, target_folder_entry, Gtk.PositionType.BOTTOM, 2, 1)
        file_entry = Gtk.Entry()
        widget_grid.attach_next_to(file_entry, file_label, Gtk.PositionType.BOTTOM, 2, 1)

        self.add(widget_grid)

    def on_source_folder_button_clicked(self):
        pass

    def on_target_folder_button_clicked(self):
        pass