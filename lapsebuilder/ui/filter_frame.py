from gi.repository import Gtk


class FilterFrame(Gtk.Frame):
    resolution_width_entry = Gtk.Entry()
    resolution_height_entry = Gtk.Entry()

    codec_label = Gtk.Label('Video Codec')
    codec_combo = Gtk.ComboBox()

    crf_label = Gtk.Label('x264 CRF')
    crf_spinbutton = Gtk.SpinButton()

    preset_label = Gtk.Label('x264 Preset')
    preset_combo = Gtk.ComboBox()

    def __init__(self, *args, **kwargs):
        super(FilterFrame, self).__init__(*args, **kwargs)

        widget_grid = Gtk.Grid()
        widget_grid.set_row_spacing(5)
        widget_grid.set_column_spacing(5)

        #Gravity
        gravity_label = Gtk.Label('Gravity')
        gravity_label.set_alignment(0.02, 0.5)
        widget_grid.attach(gravity_label, 3, 1, 3, 1)
        gravity_store = Gtk.ListStore(int, str)
        gravity_store.append([1, 'CENTER'])
        gravity_store.append([2, 'TOP'])
        gravity_store.append([3, 'BOTTOM'])
        gravity_renderer = Gtk.CellRendererText()
        gravity_combo = Gtk.ComboBox.new_with_model(gravity_store)
        gravity_combo.set_active(0)
        gravity_combo.pack_start(gravity_renderer, True)
        gravity_combo.add_attribute(gravity_renderer, "text", 1)
        widget_grid.attach_next_to(gravity_combo, gravity_label, Gtk.PositionType.BOTTOM, 3, 1)

        #Resolution
        FilterFrame.resolution_width_entry.set_editable(False)
        FilterFrame.resolution_height_entry.set_editable(False)
        resolution_label = Gtk.Label('Resolution')
        resolution_label.set_alignment(0.02, 0.5)
        widget_grid.attach_next_to(resolution_label, gravity_combo, Gtk.PositionType.BOTTOM, 3, 1)
        resolution_store = Gtk.ListStore(int, str)
        resolution_store.append([1, '1080p'])
        resolution_store.append([2, '720p'])
        resolution_store.append([3, 'Custom...'])
        resolution_renderer = Gtk.CellRendererText()
        resolution_combo = Gtk.ComboBox.new_with_model(resolution_store)
        resolution_combo.set_active(0)
        resolution_combo.connect('changed', self.on_resolution_combo_changed)
        self.on_resolution_combo_changed(resolution_combo)
        resolution_combo.pack_start(resolution_renderer, True)
        resolution_combo.add_attribute(resolution_renderer, "text", 1)
        widget_grid.attach_next_to(resolution_combo, resolution_label, Gtk.PositionType.BOTTOM, 3, 1)
        widget_grid.attach_next_to(FilterFrame.resolution_width_entry, resolution_combo, Gtk.PositionType.BOTTOM, 1, 1)
        resolution_x_label = Gtk.Label('x')
        widget_grid.attach_next_to(resolution_x_label, FilterFrame.resolution_width_entry, Gtk.PositionType.RIGHT, 1, 1)
        widget_grid.attach_next_to(FilterFrame.resolution_height_entry, resolution_x_label, Gtk.PositionType.RIGHT, 1, 1)

        v_separator = Gtk.VSeparator()
        widget_grid.attach_next_to(v_separator, gravity_label, Gtk.PositionType.RIGHT, 1, 5)

        #Framerate
        framerate_label = Gtk.Label('Framerate')
        framerate_label.set_alignment(0.02, 0.5)
        widget_grid.attach_next_to(framerate_label, v_separator, Gtk.PositionType.RIGHT, 2, 1)
        framerate_store = Gtk.ListStore(int, str)
        framerate_store.append([1, '30'])
        framerate_store.append([2, '25'])
        framerate_store.append([3, '24'])
        #framerate_renderer = Gtk.CellRendererText()
        framerate_combo = Gtk.ComboBox.new_with_model_and_entry(framerate_store)
        framerate_combo.set_entry_text_column(1)
        framerate_combo.get_child().set_text('30')
        #framerate_combo.pack_start(framerate_renderer, True)
        #framerate_combo.add_attribute(framerate_renderer, "text", 1)
        widget_grid.attach_next_to(framerate_combo, framerate_label, Gtk.PositionType.BOTTOM, 2, 1)

        #Video Codec
        FilterFrame.codec_label.set_alignment(0.02, 0.5)
        widget_grid.attach_next_to(FilterFrame.codec_label, framerate_combo, Gtk.PositionType.BOTTOM, 2, 1)
        codec_store = Gtk.ListStore(int, str)
        codec_store.append([1, 'x264'])
        codec_store.append([2, 'mpeg4'])
        codec_renderer = Gtk.CellRendererText()
        FilterFrame.codec_combo.set_model(codec_store)
        FilterFrame.codec_combo.set_active(0)
        FilterFrame.codec_combo.pack_start(codec_renderer, True)
        FilterFrame.codec_combo.add_attribute(codec_renderer, "text", 1)
        FilterFrame.codec_combo.connect("changed", self.on_video_codec_changed)
        widget_grid.attach_next_to(FilterFrame.codec_combo, FilterFrame.codec_label, Gtk.PositionType.BOTTOM, 2, 1)

        #Codec CRF
        FilterFrame.crf_label.set_alignment(0.02, 0.5)
        widget_grid.attach_next_to(FilterFrame.crf_label, FilterFrame.codec_combo, Gtk.PositionType.BOTTOM, 1, 1)
        FilterFrame.crf_spinbutton.set_digits(0)
        FilterFrame.crf_spinbutton.set_range(1.0, 23.0)
        FilterFrame.crf_spinbutton.set_increments(1.0, 1.0)
        FilterFrame.crf_spinbutton.set_numeric(True)
        FilterFrame.crf_spinbutton.set_value(10)
        widget_grid.attach_next_to(FilterFrame.crf_spinbutton, FilterFrame.crf_label, Gtk.PositionType.RIGHT, 1, 1)

        #x264 Preset
        FilterFrame.preset_label.set_alignment(0.02, 0.5)
        widget_grid.attach_next_to(FilterFrame.preset_label, FilterFrame.crf_label, Gtk.PositionType.BOTTOM, 2, 1)
        preset_store = Gtk.ListStore(int, str)
        preset_store.append([1, 'Ultra Fast'])
        preset_store.append([2, 'Super Fast'])
        preset_store.append([3, 'very Fast'])
        preset_store.append([4, 'Faster'])
        preset_store.append([5, 'Fast'])
        preset_store.append([6, 'Medium'])
        preset_store.append([7, 'Slow'])
        preset_store.append([8, 'Slower'])
        preset_store.append([9, 'Very Slow'])
        preset_renderer = Gtk.CellRendererText()
        FilterFrame.preset_combo.set_model(preset_store)
        FilterFrame.preset_combo.set_active(7)
        FilterFrame.preset_combo.pack_start(preset_renderer, True)
        FilterFrame.preset_combo.add_attribute(preset_renderer, "text", 1)
        widget_grid.attach_next_to(FilterFrame.preset_combo, FilterFrame.preset_label, Gtk.PositionType.BOTTOM, 2, 1)

        self.add(widget_grid)

    def on_resolution_combo_changed(self, combo):
        resolution_iter = combo.get_active_iter()
        if resolution_iter is not None:
            model = combo.get_model()
            row_id, name = model[resolution_iter][:2]
            if row_id == 1:
                FilterFrame.resolution_width_entry.set_text('1920')
                FilterFrame.resolution_height_entry.set_text('1080')
            elif row_id == 2:
                FilterFrame.resolution_width_entry.set_text('1280')
                FilterFrame.resolution_height_entry.set_text('720')
            elif row_id == 3:
                FilterFrame.resolution_width_entry.set_editable(True)
                FilterFrame.resolution_height_entry.set_editable(True)
                FilterFrame.resolution_width_entry.set_text('')
                FilterFrame.resolution_height_entry.set_text('')

    def on_video_codec_changed(self, combo):
        codec_iter = combo.get_active_iter()
        if codec_iter is not None:
            model = combo.get_model()
            row_id, name = model[codec_iter][:2]
            if row_id == 1:
                self.toggle_x264_settings(True)
            elif row_id == 2:
                self.toggle_x264_settings(False)

    def toggle_x264_settings(self, show_x264_settings):
        if show_x264_settings is True:
            FilterFrame.crf_label.set_visible(True)
            FilterFrame.crf_spinbutton.set_visible(True)
            FilterFrame.preset_label.set_visible(True)
            FilterFrame.preset_combo.set_visible(True)
        else:
            FilterFrame.crf_label.set_visible(False)
            FilterFrame.crf_spinbutton.set_visible(False)
            FilterFrame.preset_label.set_visible(False)
            FilterFrame.preset_combo.set_visible(False)

