#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from setuptools import setup, find_packages

setup(
    name = "woost.extensions.googleanalytics",
    version = "0.0b1",
    description = "googleanalytics extension for the Woost CMS.",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: ZODB",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Site Management"
    ],
    install_requires = [
        "woost==3.0.*",
        "oauth2client",
        "google-api-python-client"
    ],
    packages = [
        "woost.extensions.googleanalytics"
    ],
    include_package_data = True,
    zip_safe = False
)

