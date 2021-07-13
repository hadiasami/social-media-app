# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in social_media/__init__.py
from social_media import __version__ as version

setup(
	name='social_media',
	version=version,
	description='social networking sites',
	author='mohammad Jasim',
	author_email='mohjas20121997@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
