import importlib
import os
import platform


def remove_duplicates(iterable):
    s = set()
    for x in iterable:
        if x not in s:
            s.add(x)
            yield x


def run_example(example, *, size=None, title=None, backend=None, fallbacks=None):
    if backend is None:
        hint = os.environ.get('MODERNGL_EXAMPLE_WINDOW', '').strip().lower()
        if hint:
            backend = hint

    if backend is None:
        backend = 'GLWindow' if platform.system().lower() == 'windows' else 'PyQt5'

    if fallbacks is None:
        fallbacks = 'PyQt5 pygame pyglet'

    if size is None:
        size = (1280, 720)

    backends = remove_duplicates(x.lower() for x in [backend] + fallbacks.split() if x)

    for name in backends:
        try:
            module = importlib.import_module('.window._' + name, 'ModernGL.ext.examples')
            return module.run_example(example, size, title)

        except ImportError:
            pass

    raise Exception('no suitable backend found')
