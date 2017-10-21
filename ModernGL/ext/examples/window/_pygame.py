# pylint: disable-all

import time

import pygame


class WindowData:
    def __init__(self):
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

    pygame.init()
    pygame.display.set_caption(title)

    if size == 'fullscreen':
        info = pygame.display.Info()
        size = (info.current_w, info.current_h)
        pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.FULLSCREEN)

    else:
        pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)

    wnd_data = WindowData()

    width, height = size
    wnd_data.viewport = (0, 0, width, height)
    wnd_data.size = (width, height)
    wnd_data.ratio = width / height if height else 1.0
    wnd_data.mouse = (0, 0)

    start_ticks = time.perf_counter()
    last_ticks = start_ticks
    key_down = [False] * 256
    running = True

    app = example(wnd_data)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                key_down[event.key & 0xFF] = True

            elif event.type == pygame.KEYUP:
                key_down[event.key & 0xFF] = False

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
        wnd_data.time = now - start_ticks
        wnd_data.frame_time = now - last_ticks
        last_ticks = now

        mouse_x, mouse_y = pygame.mouse.get_pos()
        wnd_data.mouse = (mouse_x, height - mouse_y - 1)

        app.render()

        pygame.display.flip()
        pygame.time.wait(10)
