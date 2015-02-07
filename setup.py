#!/usr/bin/env python
# coding: utf-8
from setuptools import find_packages, setup


setup(
    author='juknsh',
    author_email='juknsh@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    install_requires=['django>=1.7'],
    keywords='python django',
    name='django-dict-response',
    packages=find_packages(),
    url='https://github.com/juknsh/django-dict-response',
    version='0.0.1',
)
