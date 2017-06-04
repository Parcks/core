#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'mock==2.0.0',
    'distro==1.0.2',
    'requests==2.13.0',
]

setup(
    name='Parcks',
    version='2.1.0',
    description="A Standardized Packages Installer",
    long_description="A Standardized Packages Installer",
    author="Setarit",
    author_email='parcks@setarit.com',
    maintainer='JValck',
    maintainer_email='parcks@setarit.com',
    url='https://github.com/Parcks',
    packages= find_packages(),
    install_requires=install_requires,
    license="Apache License 2.0",
    platforms='Linux',
    keywords='Parcks Installer',
    entry_points={
        'console_scripts': [
            'parcks = src.main:start',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop'
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)