# Copyright 2016 Adler Brediks Medrado
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import setup, find_packages


with open("requirements.txt") as reqs:
    install_requires = reqs.readlines()


setup(
    name="abbr",
    version="0.0.1",
    url="https://github.com/adlermedrado/abbr",

    author="Adler Brediks Medrado",
    author_email="abbr@adlermedrado.com.br",

    license="Apache-2.0",
    description="A client library to abbreviate string contents",
    long_description=open('README.rst').read(),

    packages=find_packages(),

    install_requires=install_requires,

    include_package_data=True,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
