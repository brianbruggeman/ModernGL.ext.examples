import GLWindow


class WindowData:
    def __init__(self, wnd):
        self._wnd = wnd

    def key_pressed(self, key):
        return self._wnd.key_pressed(key)

    def key_released(self, key):
        return self._wnd.key_released(key)

    def key_down(self, key):
        return self._wnd.key_down(key)

    def key_up(self, key):
        return self._wnd.key_up(key)

    @property
    def viewport(self):
        return self._wnd.viewport

    @property
    def size(self):
        return self._wnd.size

    @property
    def mouse(self):
        return self._wnd.mouse

    @property
    def time(self):
        return self._wnd.time

    @property
    def frame_time(self):
        return self._wnd.time_delta


def run_example(example, size, title):
    if title is None:
        title = '%s - %s - %s' % (example.__name__, 'ModernGL', 'GLWindow')

    if size == 'fullscreen':
        wnd = GLWindow.create_window(fullscreen=True, title=title)

    else:
        wnd = GLWindow.create_window(size, title=title)

    app = example(WindowData(wnd))

    while wnd.update():
        app.render()
