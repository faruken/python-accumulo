#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import (setup, find_packages)

setup(
    name="python-accumulo",
    version="0.1",
    description="Apache Accumulo client library for Python3",
    url="https://github.com/faruken/python-accumulo",
    author="faruken",
    platforms="any",
    zip_safe=False,
    license="Apache Software License",
    keywords="accumulo",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    packages=find_packages(exclude=["tests", "examples"]),
    install_requires=[
        "thrift"
    ],
    extras_requires={
        "test": ["coverage", "pytest", "pytest-cov"]
    }
)
