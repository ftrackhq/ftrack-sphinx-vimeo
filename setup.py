# :coding: utf-8
# :copyright: Copyright (c) 2014 ftrack

import os

from setuptools import setup, find_packages


readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')
packages_path = os.path.join(os.path.dirname(__file__), 'source')

# General configuration.
configuration = dict(
    name='ftrack-sphinx-vimeo',
    version=0.1,
    description='Sphinx vimeo plugin.',
    long_description=open(readme_path).read(),
    keywords='sphinx, vimeo',
    url='https://bitbucket.org/ftrack/ftrack-sphinx-vimeo',
    author='ftrack',
    author_email='support@ftrack.com',
    license='Apache License (2.0)',
    package_dir={
        '': 'source'
    },
    packages=find_packages(packages_path)
)

# Call main setup.
setup(**configuration)
