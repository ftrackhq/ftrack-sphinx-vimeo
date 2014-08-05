# :coding: utf-8
# :copyright: Copyright (c) 2014 ftrack
import os

from setuptools import setup


README_PATH = os.path.join(os.path.dirname(__file__), 'README.rst')

# General configuration.
configuration = dict(
    name='ftrack-sphinx-vimeo',
    version=0.1,
    description='Sphinx vimeo plugin.',
    long_description=open(README_PATH).read(),
    keywords='sphinx, vimeo',
    url='https://bitbucket.org/ftrack/ftrack-sphinx-vimeo',
    author='ftrack',
    author_email='support@ftrack.com',
    license='Apache License (2.0)',
    package_dir={
        '': 'source'
    }
)

# Call main setup.
setup(**configuration)