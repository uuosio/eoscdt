import os
import sys
import platform
from setuptools import find_packages
from distutils.core import setup

def patch():
    '''
    patch CDTWasmToolchain.cmake and cdt-config.cmake
    '''
    if not os.path.exists('pysrc/release/lib/cmake/cdt/CDTWasmToolchain.cmake'):
        return
    get_cdt_root_dir = '''
execute_process(
   COMMAND eoscdt-get-root-dir
            OUTPUT_VARIABLE CDT_ROOT
            OUTPUT_STRIP_TRAILING_WHITESPACE
            ERROR_STRIP_TRAILING_WHITESPACE
            RESULT_VARIABLE CDT_ROOT_RESULT
)
'''

    with open('pysrc/release/lib/cmake/cdt/CDTWasmToolchain.cmake', 'r') as f:
        data = f.read()
        data = data.replace('set(CMAKE_FIND_ROOT_PATH "_PREFIX_")', f'{get_cdt_root_dir}\nset(CMAKE_FIND_ROOT_PATH "${{CDT_ROOT}}/lib/cmake/cdt")\n')
    with open('pysrc/release/lib/cmake/cdt/CDTWasmToolchain.cmake', 'w') as f:
        f.write(data)

    with open('pysrc/release/lib/cmake/cdt/cdt-config.cmake', 'r') as f:
        data = f.read()
        data = get_cdt_root_dir + data
    with open('pysrc/release/lib/cmake/cdt/cdt-config.cmake', 'w') as f:
        f.write(data)

patch()

release_files = []
for root, dirs, files in os.walk("pysrc/release"):
    for f in files:
        release_files.append(os.path.join(root.replace('pysrc/', ''), f))

version = platform.python_version_tuple()
version = '%s.%s' % (version[0], version[1])

setup(
    name="eoscdt",
    version="0.1.2",
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
