#!/usr/bin/env python
#
# Copyright 2010-2012 Alexandre Fiori
# based on the original Tornado by Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sys
import setuptools

setuptools.setup(
    name="cyclone",
    version="0.8",
    packages=["cyclone", "cyclone.redis"],
    #install_requires=["twisted"],
    author="fiorix",
    author_email="fiorix@gmail.com",
    url="http://cyclone.io/",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="Non-blocking web server. A facebook's Tornado on top of Twisted.",
    keywords="web server non-blocking python twisted facebook tornado",
    package_data={"cyclone":["appskel.zip"]},
)
