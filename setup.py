# -*- coding: utf-8 -*-
import os
from setuptools import setup

install_requires = [
    'Pillow==9.5.0',
    "pypicgo==1.2.1",
    "flask==2.3.3",
]

if os.path.exists('VERSION'):
    with open('VERSION') as f:
        version = f.read().strip()
else:
    version = '0.0.1'

setup(
    name='ccbs-picbed',
    version=version,
    packages=['ccbs_picbed'],
    include_package_data=True,
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        ccbs-picbed=ccbs_picbed.main:cli
    ''',
)
