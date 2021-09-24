#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup

NAME = 'nevo'
VERSION = '0.0.1'
AUTHOR = 'Sid Chaubal'
AUTHOR_EMAIL = 's.p.chaubal@student.vu.nl'
DESCRIPTION = ''
KEYWORDS = 'neuroevolution neural-networks python3 ml ai machine-learning artificial-intelligence'
PYTHON_VERSION = '>=3.7.0'
REQUIRED = ['docopt', 'termcolor']
EXCLUDE = ['tests', '*.tests', '*.tests.*', 'tests.*']
EXTRAS = {}

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = '\n' + f.read()

setup(
  name = NAME,
  version = VERSION,
  description = DESCRIPTION,
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = AUTHOR,
  author_email = AUTHOR_EMAIL,
  python_requires = PYTHON_VERSION,
  packages = find_packages(exclude = EXCLUDE),
  py_modules = ['pydoku'],
  entry_points = {
    'console_scripts': [
      'NEVO = nevo.cli:interpret'
    ]
  },
  install_requires = REQUIRED,
  extras_require = EXTRAS,
  include_package_data = True,
  license = 'MIT',
  classifiers = [
    'License :: OSI Approved :: MIT License',
    'Development Status :: 4 - Beta',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering :: Artificial Intelligence'
  ]
)