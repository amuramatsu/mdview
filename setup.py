#!/usr/bin/env python

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_version(filename):
    """Extract __version__ from file by parsing it."""
    with open(filename) as fp:
        for line in fp:
            if line.startswith('__version__'):
                namespace = {}
                exec(line, namespace)
                return namespace['__version__']

setup(
    name='mdview',
    version=get_version('mdview/__init__.py'),
    description='Markdown viewer',
    url='https://github.com/guyru/mdview',
    author='Guy Rutenberg',
    author_email='guyrutenberg@gmail.com',
    license = 'GPLv3+',
    packages=['mdview'],
    entry_points = {
        'console_scripts': [
            'mdview = mdview:run',
        ]
    },
    long_description=read('README.rst'),
    package_data={'mdview': ['static/*.js', 'static/*.css', 'static/*.ico', 'templates/*.html']},
    install_requires = ['markdown', 'flask', 'Pygments'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Framework :: Flask',
        ],
)

