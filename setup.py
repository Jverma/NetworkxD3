#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import sys

sys.path.insert(0, 'NetworkxD3')

sys.path.pop(0)

packages = ['NetworkxD3']

setup(
	name='networkxD3',
	version='0.20',
	author='Janu Verma',
	author_email='jv367@cornell.edu',
	description='D3 JavaScript networkx Graphs',
	url='https://github.com/Jverma/NetworkxD3',
	platforms=['Linux','Mac OSX', 'Windows', 'Unix'],
	classifiers=[
	'Development Status :: 3 - Alpha',
	'Intended Audience :: Developers',
	'License :: MIT License',
	'Operating System :: OS Independent',
	'Progamming Language :: Python',
	'Topic :: Software Development :: Libraries :: Python Modules'],
	packages=packages,
	license='MIT'
	)			
