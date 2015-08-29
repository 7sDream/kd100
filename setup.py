#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import ast

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def extract_version():
    with open('kd100/__init__.py', 'rb') as f_version:
        ast_tree = re.search(
            r'__version__ = (.*)',
            f_version.read().decode('utf-8')
        ).group(1)
        if ast_tree is None:
            raise RuntimeError('Cannot find version information')
        return str(ast.literal_eval(ast_tree))

with open('README.rst', 'rb') as f_readme:
    readme = f_readme.read().decode('utf-8')

packages = ['kd100']

version = extract_version()

setup(
    name='kd100',
    version=version,
    keywords=['internet', 'query', 'express', 'http'],
    description='I\'m a small script that help you get '
                'express package information use kuaidi100.com api.',
    long_description=readme,
    author='7sDream',
    author_email='didislover@gmail.com',
    license='MIT',
    url='https://github.com/7sDream/kd100',

    install_requires=[],
    packages=packages,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Information Technology',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],

    entry_points={
        'console_scripts': [
            'kd100 = kd100.kd100:main'
        ]
    }
)
