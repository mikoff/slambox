from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout


class SymforceConan(ConanFile):
    name = "symforce"
    version = "0.1"
    license = "Apache-2.0"
    url = "https://github.com/symforce-org/symforce"
    description = "Fast symbolic computation & code generation for robotics."
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = ["patches/*"]

    def requirements(self):
        self.requires("eigen/3.4.0")

    def source(self):
        # Clone directly into the source folder
        self.run("git clone https://github.com/symforce-org/symforce.git .")

    def layout(self):
        # CMakeLists.txt is at the repo root.
        cmake_layout(self, src_folder=".")

    def generate(self):
        # Generate both toolchain and dependency files
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

    def package_info(self):
        self.cpp_info.libs = ["symforce_cholesky", "symforce_gen", "symforce_opt", "symforce_slam"]
