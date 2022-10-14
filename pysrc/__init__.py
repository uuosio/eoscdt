import os
import sys
import shlex
import platform
import subprocess
import sysconfig
import argparse

__version__ = "0.1.2"

cdt_install_dir = os.path.dirname(os.path.realpath(__file__))

def get_platform_name():
    if platform.system() == "Linux":
        return "manylinux1_x86_64"
    elif platform.system() == "Windows":
        return "win-amd64"
    elif platform.system() == "Darwin":
        return "macosx_10_15_x86_64"
    else:
        raise Exception("Unknown")

def init():
    dir_name = os.path.dirname(os.path.realpath(__file__))
    dir_name = os.path.join(dir_name, "release")
    if os.path.exists(dir_name):
        return
    print('due to the file size limit of pypi, eoscdt installed from pypi does not include binary release. reinstalling...')
    from pip._internal.cli.main import main as _main
    platfrom_name = get_platform_name()
    _main(['install', '--force-reinstall', f'https://github.com/uuosio/pycdt/releases/download/v{__version__}/eoscdt-{__version__}-py3-none-{platfrom_name}.whl'])

def run_cmd(cmd: str) -> int:
    init()
    dir_name = os.path.dirname(os.path.realpath(__file__))
    dir_name = os.path.join(dir_name, "release")
    cmd = os.path.join(dir_name, f"bin/{cmd}")
    sys.argv[0] = cmd
    return subprocess.call(sys.argv, stdout=sys.stdout, stderr=sys.stderr)

def run_cdt_init():
    return run_cmd('cdt-init')

def run_cdt_cpp():
    return run_cmd('cdt-cpp')

def run_cdt_cc():
    return run_cmd('cdt-cc')

def run_cdt_pp():
    return run_cmd('cdt-pp')

def run_cdt_ld():
    return run_cmd('cdt-ld')

def run_eos_cdt():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser')

    init = subparsers.add_parser('init')
    # init.add_argument('project_name')

    build = subparsers.add_parser('build')
    build.add_argument('--dir-name', default=".")
    build.add_argument('-d', '--debug', action='store_true', help='set to true to enable debug build')
    result = parser.parse_args()

    if not result or not result.subparser:
        parser.print_usage()
        sys.exit(-1)
    if result.subparser == "init":
        init()
    elif result.subparser == "build":
        cur_dir = os.path.abspath(os.curdir)
        cdt_dir = os.path.join(cdt_install_dir, 'release/lib/cmake/cdt')
        os.chdir('build')
        cmd = f'cmake -Dcdt_DIR={cdt_dir} {cur_dir}'
        print(cmd)
        cmd = shlex.split(cmd)
        return subprocess.call(cmd)

def run_eos_cdt_get_root_dir():
    print(os.path.join(cdt_install_dir, 'release'))

def run_eos_cdt_get_dir():
    print(os.path.join(cdt_install_dir, 'release/lib/cmake/cdt'))
