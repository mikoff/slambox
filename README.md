# Repo for experiments on CV and SLAM

## Python
To activate conan-build packages, like `symforce`, call:
```bash
source /workspace/build/generators/conanrun.sh
```
If you want to use jupyter just open a notebook and pick Jupyter kernel, associated with `symforce`.


## C++ build
Build & run everything
```bash
conan build . --build=missing
```

If you want to set some settings, change configuration set the appropriate settings, e.g.:
```bash
conan build . --build=missing -s build_type=Release -s "slambox/*:build_type=Release" -c tools.build:skip_test=False
```
