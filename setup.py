#!/usr/bin/env python

"""Setup script for TemplatePythonDemo."""

import setuptools

from temppydemo import __project__, __version__

import os
if os.path.exists('README.rst'):
    README = open('README.rst').read()
else:
    README = ""  # a placeholder until README is generated on release
CHANGES = open('CHANGES.md').read()


setuptools.setup(
    name=__project__,
    version=__version__,

    description="TemplatePythonDemo is a Python package template.",
    url='https://github.com/robertberrington/template-python-demo',
    author='Robert Berrington',
    author_email='robertberringtoniii@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    long_description=(README + '\n' + CHANGES),
    license='MIT',
    classifiers=[
        # TODO: update this list to match your application: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    install_requires=open('requirements.txt').readlines(),
)
