
import os
import sys

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy


class SymforceConan(ConanFile):
    name = "symforce"
    version = "0.1"
    license = "Apache-2.0"
    url = "https://github.com/symforce-org/symforce"
    description = "Fast symbolic computation & code generation for robotics."
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = ["patches/*"]

    def build_requirements(self):
        self.tool_requires("cmake/[<=3.26]")

    def requirements(self):
        self.requires("eigen/3.4.0")

    def source(self):
        # Clone symforce repository
        self.run("git clone https://github.com/symforce-org/symforce.git .")

    def layout(self):
        # Use the repository root as the source folder.
        cmake_layout(self, src_folder=".")

    def generate(self):
        # Optionally install Python dependencies if not already available;
        # (if you prefer to install them externally, you can remove this step)
        self.run(f"{sys.executable} -m pip install -r requirements_build.txt",
                 cwd=self.source_folder)

        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

        copy(self, pattern="LICENSE", dst=os.path.join(self.package_folder, "licenses"), src=self.source_folder)
        copy(self, pattern="*", src=os.path.join(self.source_folder, "symforce"), dst=os.path.join(self.package_folder, "python", "symforce"))
        copy(self, pattern="*", src=os.path.join(self.source_folder, "third_party", "skymarshal", "skymarshal"), dst=os.path.join(self.package_folder, "python", "skymarshal"))
        copy(self, pattern="*", src=os.path.join(self.source_folder, "gen", "python", "sym"), dst=os.path.join(self.package_folder, "python", "sym"))
        copy(self, pattern="*", src=os.path.join(self.build_folder, "lcmtypes", "python2.7", "lcmtypes"), dst=os.path.join(self.package_folder, "python", "lcmtypes"))
        copy(self, pattern="*", src=os.path.join(self.build_folder, "pybind"), dst=os.path.join(self.package_folder, "python"))

    def package_info(self):
        self.cpp_info.libs = ["symforce_cholesky", "symforce_gen", "symforce_opt", "symforce_slam"]

        python_folder = os.path.join(self.package_folder, "python")
        self.env_info.PYTHONPATH.append(python_folder)
