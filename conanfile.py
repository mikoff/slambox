import os

from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake, CMakeDeps, CMakeToolchain


class SlamBoxRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def requirements(self):
        self.requires("boost/1.84.0")
        self.requires("ceres-solver/2.2.0")
        self.requires("eigen/3.4.0")
        self.requires("gtsam/4.2")
        # self.requires("libpng/1.6.40", override=True)
        self.requires("opencv/4.10.0")
        # self.requires("pulseaudio/14.2")
        self.test_requires("gtest/1.11.0")

    def build_requirements(self):
        self.tool_requires("cmake/3.28.1")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if not self.conf.get("tools.build:skip_test", default=False):
            test_folder = os.path.join("tests")
            self.run(os.path.join(test_folder, "dummy_test"))
