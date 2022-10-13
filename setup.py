import os
import sys
import platform
from setuptools import find_packages
from distutils.core import setup

release_files = []
for root, dirs, files in os.walk("pysrc/release"):
    for f in files:
        release_files.append(os.path.join(root.replace('pysrc/', ''), f))

version = platform.python_version_tuple()
version = '%s.%s' % (version[0], version[1])

setup(
    name="eoscdt",
    version="0.1.0",
    description="eoscdt project",
    author='The EOSCDT Team',
    license="MIT",
    packages=[
        'eoscdt',
    ],
    package_dir={
        'eoscdt': 'pysrc',
    },
    package_data={'eoscdt': release_files},

    install_requires=[
    ],
    tests_require=[],
    include_package_data=True
)
