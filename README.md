# Repo for experiments on CV and SLAM

## Python
To activate Conan-built packages like `symforce`, run:
```bash
source /workspace/build/generators/conanrun.sh
```
To use Jupyter, open a notebook and select the kernel associated with `symforce` using drop-down VSCode menu.


## C++ build
To build and run everything:
```bash
conan build . --build=missing
```

To set specific configurations, adjust the settings as needed. For example:
```bash
conan build . --build=missing -s build_type=Release -s "slambox/*:build_type=Release" -c tools.build:skip_test=False
```
