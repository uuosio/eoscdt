# eoscdt

## Installation
Linux & MacOS X

```
python3 -m pip install -U eoscdt
eoscdt init
```

Windows

```
python -m pip install -U eoscdt
eoscdt init
```

## Quick start
```
cdt-init --project hello
cd hello
mkdir build
cd build
cmake -Dcdt_DIR=`cdt-get-dir` ..
make -j$(nproc)
```

## About Windows

It's recommended to use [msys2](https://www.msys2.org) as a build environment.
After installation, click `start` button on the Windows taskbar, search for `msys2 clang64` and open it.
Then run the following command to install dependencies.

```
pacman --noconfirm -S git
pacman --noconfirm -S --needed base-devel mingw-w64-clang-x86_64-clang
pacman --noconfirm -S mingw-w64-clang-x86_64-gdb mingw-w64-clang-x86_64-compiler-rt
pacman --noconfirm -S mingw-w64-clang-x86_64-boost
pacman --noconfirm -S mingw-w64-clang-x86_64-cmake
pacman --noconfirm -S mingw-w64-clang-x86_64-python
pacman --noconfirm -S mingw-w64-clang-x86_64-python-pip
```

Finally, install eoscdt
```
python -m pip install -U eoscdt
eoscdt init
```
