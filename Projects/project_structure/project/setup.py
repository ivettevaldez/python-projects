try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'project',
    'description': 'My Project.',
    'author': 'Silvia Valdez',
    'author_email': 'silvia.valdez.e@gmail.com',
    'url': 'https://github.com/silvia-valdez/PythonProjects',
    'download_url': 'https://github.com/silvia-valdez/PythonProjects',
    'version': '0.1',
    'packages': ['src'],
    'install_requires': ['nose2'],
    'scripts': []
}

setup(**config)
