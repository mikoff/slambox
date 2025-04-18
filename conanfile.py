import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain
from conan.tools.env import VirtualRunEnv


class SlamBoxRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("boost/1.84.0")
        self.requires("ceres-solver/2.2.0")
        self.requires("eigen/3.4.0")
        self.requires("gtsam/4.2")
        self.requires("opencv/4.10.0")
        self.requires("symforce/0.1@youruser/testing")
        self.test_requires("gtest/1.15.0")

    def build_requirements(self):
        self.tool_requires("cmake/3.28.1")

    def layout(self):
        self.folders.build = "build"
        self.folders.generators = os.path.join(self.folders.build, "generators")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["CMAKE_EXPORT_COMPILE_COMMANDS"] = "ON"
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

        venv = VirtualRunEnv(self)
        venv.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if not self.conf.get("tools.build:skip_test", default=False):
            test_folder = os.path.join("tests")
            self.run(os.path.join(test_folder, "dummy_test"))

    def package(self):
        # (Optional) you may add package() step here if needed.
        pass

    def package_info(self):
        # (Optional) if packaging artifacts is desired, configure package_info accordingly.
        pass
