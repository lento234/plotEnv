#! /usr/bin/env python

import os
import configparser
from setuptools import setup, find_packages

conf = configparser.ConfigParser()
conf.read(['setup.cfg'])
metadata = dict(conf.items('metadata'))

# Get the long description from the README file
with open(os.path.join('README.md'), encoding='utf-8') as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name=metadata['package_name'],
        description=metadata['description'],
        version=metadata['version'],
        url=metadata['url'],
        author=metadata['author'],
        author_email=metadata['author_email'],
        long_description=long_description,
    	long_description_content_type='text/markdown',
        license=metadata['license'],
        packages=find_packages(),
        #install_requires=check_dependencies(),
        classifiers=[
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Topic :: Scientific/Engineering :: Visualization',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 3.8',
        ],
    )
