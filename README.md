[CDT](https://github.com/uuosio/cdt) Release with Python Wheel Package

# EOSCDT

## Installation
Linux & MacOS X

```
python3 -m pip install -U eoscdt
eoscdt check
```

Windows

```
python -m pip install -U eoscdt
eoscdt check
```

## Quick start
```
cdt-init --project hello
cd hello
mkdir build
cd build
cmake -Dcdt_DIR=`cdt-get-dir` -G"Unix Makefiles" ..
make -j$(nproc)
```

If everything goes well, you will find hello.wasm and hello.abi in your build/hello directory.

## About Windows

### Setup MSYS2 Development Environment

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
eoscdt check
```

If you are using Visual Studio Code as an IDE, you can use msys2 bash as your terminal.
search for `Preferences: Open User Settings(JSON)` and open it. Add the following configuration for msys2
```
"terminal.integrated.env.windows": {
    "MSYSTEM": "CLANG64",
    "CHERE_INVOKING": "1",
    "MSYS2_PATH_TYPE": "inherit",
    "LIBRARY_PATH": "/clang64/lib"
},
"terminal.integrated.profiles.windows": {
    "msys2": {
        "path": "G:\\msys64\\usr\\bin\\bash.exe",
        "args": ["--login", "-i"]
    }
}
```

Change `G:\\msys64\\usr\\bin\\bash.exe` to the location of bash.exe you installed.

For more details, please see [Terminal Profiles](https://code.visualstudio.com/docs/terminal/profiles#_configuring-profiles)

### Official Python Development Environment

If you have downloaded and installed python from [official python website](https://www.python.org/downloads/windows), don't forget to enable `Add Python to environment variables` option during the installation, otherwise cmd.exe will have problem finding executable programs of CDT.

Launch cmd.exe to install eoscdt, cmake and ninja

```
pip install -U eoscdt
eoscdt check
pip install cmake
pip install ninja
```

Also you need to change `project(xxx)` to `project(xxx NONE)` in your CMakeLists.txt to pass the compiler checking if you didn't install other compiler such as Visual Studio on your Windows.

Here is a minimal steps about building smart contracts with only cmake and ninja installed

```
cdt-init --project hello
```

add `project(hello NONE)` to CMakeLists.txt

get the cdt directory

```
cdt-get-dir
```

```
mkdir build
cd build
cmake -Dcdt_DIR="cdt dir output by the previous step" -GNinja ..
ninja
```
