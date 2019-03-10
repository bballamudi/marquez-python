# coding: utf-8

"""
    Marquez

    Marquez is an open source **metadata service** for the **collection**, **aggregation**, and **visualization** of a data ecosystem's metadata.  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import find_packages, setup  # noqa: H301

NAME = "marquez-python"
VERSION = "0.1.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi",
            "python-dateutil", "marquez-python-codegen"]

setup(
    name=NAME,
    version=VERSION,
    description="Marquez Python Client",
    author_email="",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Marquez"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Marquez-Python is an open source library for building clients that
    interact with a running Marquez instance.
    """
)
