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
    name="pycdt",
    version="0.1.0",
    description="pycdt project",
    author='The PYCDT Team',
    license="MIT",
    packages=[
        'pycdt',
    ],
    package_dir={
        'pycdt': 'pysrc',
    },
    package_data={'pycdt': release_files},

    install_requires=[
    ],
    tests_require=[],
    include_package_data=True
)
