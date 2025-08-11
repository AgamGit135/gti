#!/usr/bin/env python3

from setuptools import setup

setup(
    name='gti',
    version='1.0',
    packages=['gti'],
    entry_points={
        'console_scripts': [
            'gti = gti.cli:main',
        ],
    }
)