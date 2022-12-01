#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='ebj2',
    version='v0.0.1',
    description='Embedded Binary JSON',
    long_description=(open('README.md').read()),
    long_description_content_type="text/markdown",
    author='urain39',
    author_email='urain39@qq.com',
    license='MIT',
    packages=find_packages(),
    platforms=["all"],
    url='https://gitlab.com/urain39/ebj2',
    keywords=['json', 'binary-json', 'embedded'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
