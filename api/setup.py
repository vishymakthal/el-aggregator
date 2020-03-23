# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "el_aggregator_api"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="El Aggregator API",
    author_email="vishy787@gmail.com",
    url="",
    keywords=["Swagger", "El Aggregator API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/api.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['el_aggregator_server=server.__main__:main']},
    long_description="""\
    This is the definition for the El Aggregator Data API.
    """
)

