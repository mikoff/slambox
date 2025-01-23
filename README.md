# Repo for experiments on CV and SLAM

Build & run everything
```
conan profile detect
conan build . --build=missing
```

If you want to set some settings, change configuration set the appropriate settings, e.g.:
```
conan build . --build=missing -s build_type=Release -s "slambox/*:build_type=Release" -c tools.build:skip_test=False
```