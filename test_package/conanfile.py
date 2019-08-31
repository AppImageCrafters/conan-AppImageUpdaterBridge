import os

from conans import ConanFile, CMake, tools


class AppimageupdatebridgeTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_paths"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_PROJECT_PackageTest_INCLUDE"] = self.build_folder + "/conan_paths.cmake"
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            self.run(".%sexample" % os.sep)
