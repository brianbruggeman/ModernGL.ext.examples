# pylint: disable-all

import time

import pyglet


class WindowData:
    def __init__(self):
        self._start_ticks = None
        self._last_ticks = None
        self.time = None
        self.frame_time = None
        self.viewport = None
        self.size = None
        self.ratio = None
        self.mouse = None

        self._key_state = [0] * 256

    def key_pressed(self, key):
        return self._key_state[key if type(key) is int else ord(key)] == 1

    def key_released(self, key):
        return self._key_state[key if type(key) is int else ord(key)] == 3

    def key_down(self, key):
        return self._key_state[key if type(key) is int else ord(key)] != 0

    def key_up(self, key):
        return self._key_state[key if type(key) is int else ord(key)] == 0


def run_example(example, size, title):
    if title is None:
        title = '%s - %s - %s' % (example.__name__, 'ModernGL', 'pygame')

    fullscreen = (size == 'fullscreen')
    wnd = pyglet.window.Window(caption=title, fullscreen=fullscreen)

    if fullscreen:
        size = wnd.get_size()

    wnd_data = WindowData()

    width, height = size
    wnd_data.viewport = (0, 0, width, height)
    wnd_data.size = (width, height)
    wnd_data.ratio = width / height if height else 1.0
    wnd_data.mouse = (0, 0)

    wnd_data._start_ticks = time.perf_counter()
    wnd_data._last_ticks = wnd_data._start_ticks
    key_down = [False] * 256

    app = example(wnd_data)

    # TODO: subclass pyglet Window

    @wnd.event
    def on_key_press(symbol, modifiers):
        key_down[symbol & 0xFF] = True

    @wnd.event
    def on_key_release(symbol, modifiers):
        key_down[symbol & 0xFF] = False

    def update(dt):
        for i in range(256):
            if key_down[i]:
                if wnd_data._key_state[i] in (0, 1):
                    wnd_data._key_state[i] += 1

                elif wnd_data._key_state[i] == 3:
                    wnd_data._key_state[i] = 1

            else:
                if wnd_data._key_state[i] in (1, 2):
                    wnd_data._key_state[i] = 3

                elif wnd_data._key_state[i] == 3:
                    wnd_data._key_state[i] = 0

        now = time.perf_counter()
        wnd_data.time = now - wnd_data._start_ticks
        wnd_data.frame_time = now - wnd_data._last_ticks
        wnd_data._last_ticks = now

        # TODO: mouse

        app.render()

    pyglet.clock.schedule_interval(update, 1.0 / 60.0)
    pyglet.app.run()
