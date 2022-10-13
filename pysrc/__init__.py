import os
import sys
import shlex
import platform
import subprocess
import sysconfig
import argparse

__version__ = "0.1.0"

def run_cmd(cmd: str) -> int:
    dir_name = os.path.dirname(os.path.realpath(__file__))
    dir_name = os.path.join(dir_name, "release")
    cmd = os.path.join(dir_name, f"bin/{cmd}")
    sys.argv[0] = cmd
    return subprocess.call(sys.argv, stdout=sys.stdout, stderr=sys.stderr)

def run_cdt_cpp():
    return run_cmd('cdt-cpp')

def run_cdt_cc():
    return run_cmd('cdt-cc')

def run_cdt_pp():
    return run_cmd('cdt-pp')

def run_cdt_ld():
    return run_cmd('cdt-ld')
