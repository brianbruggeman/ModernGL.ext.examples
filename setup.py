import platform
import os

PLATFORM = platform.system().lower()

if os.environ.get('READTHEDOCS') == 'True':
    from distutils.core import setup

else:
    from setuptools import setup

install_requires = ['ModernGL']

if PLATFORM == 'windows':
    if 'NO_GLWINDOW' not in os.environ:
        install_requires.append('GLWindow')

if 'NO_PYQT5' not in os.environ:
    install_requires.append('PyQt5')

if 'NO_PYGAME' not in os.environ:
    install_requires.append('pygame')

if 'NO_PYRR' not in os.environ:
    install_requires.append('Pyrr')

if 'NO_PILLOW' not in os.environ:
    install_requires.append('Pillow')

setup(
    name='ModernGL.ext.examples',
    version='1.1.0',
    author='Szabolcs Dombi',
    author_email='cprogrammer1994@gmail.com',
    description='ModernGL extension',
    url='https://github.com/cprogrammer1994/ModernGL.ext.examples',
    license='MIT',
    packages=['ModernGL.ext.examples', 'ModernGL.ext.examples.window'],
    install_requires=install_requires,
    platforms=['any'],
)
