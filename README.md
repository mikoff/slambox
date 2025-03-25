# Repo for experiments on CV and SLAM

## Python
Import all python modules:
```bash
source tools/activate-dev-env.sh
```
then run ipython and experiment with `symforce` or other packages.


## C++ build
Build & run everything
```bash
conan build . --build=missing
```

If you want to set some settings, change configuration set the appropriate settings, e.g.:
```bash
conan build . --build=missing -s build_type=Release -s "slambox/*:build_type=Release" -c tools.build:skip_test=False
```