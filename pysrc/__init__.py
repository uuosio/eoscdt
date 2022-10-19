import os
import sys
import shlex
import shutil
import platform
import subprocess
import sysconfig
import argparse
import multiprocessing
import tempfile
from pip._internal.cli.main import main as _main

__version__ = "0.1.7"

cdt_install_dir = os.path.dirname(os.path.realpath(__file__))

def get_platform_name():
    if platform.system() == "Linux":
        return "manylinux1_x86_64"
    elif platform.system() == "Windows":
        return "win_amd64"
    elif platform.system() == "Darwin":
        return "macosx_10_15_x86_64"
    else:
        raise Exception("Unknown")

def run_reinstall_process(whl: str):
    reinstall_code = f'''
import os
import shutil
from pip._internal.cli.main import main as _main
print('start reinstallation')
_main(['install', '--force-reinstall', '{whl}'])
shutil.rmtree(os.path.dirname('{whl}'))
print('done!')
'''
    subprocess.Popen([sys.executable, '-c', reinstall_code], close_fds=True)
    sys.exit(0)

def check_release(check: bool = False):
    dir_name = os.path.dirname(os.path.realpath(__file__))
    dir_name = os.path.join(dir_name, "release")
    if os.path.exists(dir_name):
        return
    if check:
        print('''
Due to the file size limit of pypi, eoscdt installed from pypi does not include binary release. reinstalling.
press Ctrl+C to cancel the installation.
        ''')
    else:
        print('''
Due to the file size limit of pypi, eoscdt installed from pypi does not include binary release. reinstalling.
press Ctrl+C to cancel the installation.
You need to restart the command after the installation finished.
        ''')
    platfrom_name = get_platform_name()
    whl = f'eoscdt-{__version__}-py3-none-{platfrom_name}.whl'
    tmp_dir = tempfile.mkdtemp()
    dest_path = os.path.join(tmp_dir, whl)
    # print(dest_path)
    cmd = [
        'download',
        f'--platform={platfrom_name}',
        '--only-binary=:all:',
        '--dest', tmp_dir,
        f'https://github.com/uuosio/eoscdt/releases/download/v{__version__}/{whl}'
    ]
    # print(cmd)
    _main(cmd)
    if not os.path.exists(dest_path):
        raise Exception('download failed!')
    if platform.system() == 'Windows': # msys2 clang64 platform, need to rename whl file name to pass pip checking
        dest_path2 = os.path.join(tmp_dir, f'eoscdt-{__version__}-py3-none-any.whl')
        shutil.move(dest_path, dest_path2)
        dest_path = dest_path2
    run_reinstall_process(dest_path)

def run_cmd(cmd: str) -> int:
    check_release()
    dir_name = os.path.dirname(os.path.realpath(__file__))
    dir_name = os.path.join(dir_name, "release")
    cmd = os.path.join(dir_name, f"bin/{cmd}")
    sys.argv[0] = cmd
    return subprocess.call(sys.argv, stdout=sys.stdout, stderr=sys.stderr)

def run_init():
    return run_cmd('cdt-init')

def run_cpp():
    return run_cmd('cdt-cpp')

def run_cc():
    return run_cmd('cdt-cc')

def run_pp():
    return run_cmd('cdt-pp')

def run_ld():
    return run_cmd('cdt-ld')

def run_abidiff():
    return run_cmd('cdt-abidiff')

def run_ranlib():
    return run_cmd('llvm-ranlib')

def run_ar():
    return run_cmd('llvm-ar')

def run_nm():
    return run_cmd('llvm-nm')

def run_objcopy():
    return run_cmd('llvm-objcopy')

def run_objdump():
    return run_cmd('llvm-objdump')

def run_readobj():
    return run_cmd('llvm-readobj')

def run_readelf():
    return run_cmd('llvm-readelf')

def run_strip():
    return run_cmd('llvm-strip')

def run_pp():
    return run_cmd('eosio-pp')

def run_wast2wasm():
    return run_cmd('eosio-wast2wasm')

def run_wasm2wast():
    return run_cmd('eosio-wasm2wast')

def run_eos_cdt():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser')

    check_parser = subparsers.add_parser('check')
    # init.add_argument('project_name')

    build = subparsers.add_parser('build')
    build.add_argument('--dir-name', default=".")
    build.add_argument('-d', '--debug', action='store_true', help='set to true to enable debug build')
    result = parser.parse_args()

    if not result or not result.subparser:
        parser.print_usage()
        sys.exit(-1)
    if result.subparser == "check":
        check_release(True)
    elif result.subparser == "build":
        cur_dir = os.path.abspath(os.curdir)
        cdt_dir = os.path.join(cdt_install_dir, 'release/lib/cmake/cdt')
        if not os.path.exists('build'):
            os.mkdir('build')
        cur_path = os.path.abspath(os.curdir)
        cur_dir = os.path.basename(cur_path)
        if not cur_dir == 'build':
            os.chdir('build')
        cmd = f'cmake -Dcdt_DIR={cdt_dir} -GNinja ..'
        print(cmd)
        cmd = shlex.split(cmd)
        ret = subprocess.call(cmd)
        if ret != 0:
            sys.exit(ret)
        cpu_count = multiprocessing.cpu_count()
        # ret = subprocess.call(['make', f'-j{cpu_count}'])
        ret = subprocess.call(['ninja'])
        sys.exit(ret)

def run_eos_cdt_get_root_dir():
    print(os.path.join(cdt_install_dir, 'release'))

def run_eos_cdt_get_dir():
    print(os.path.join(cdt_install_dir, 'release/lib/cmake/cdt'))
