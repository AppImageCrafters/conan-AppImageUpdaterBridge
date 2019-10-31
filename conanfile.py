from conans import ConanFile, CMake, tools


class AppImageUpdaterBridgeConan(ConanFile):
    name = "AppImageUpdaterBridge"
    version = "1.1.6"
    license = "BSD-3-Clause"
    author = "Alexis Lopez Zubieta contact@azubieta.net"
    url = "https://github.com/antony-jr/AppImageUpdaterBridge/issues"
    description = "Qt5 library for updating AppImages"
    topics = ("AppImage", "update")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "NO_GUI": [True, False], "LOGGING_DISABLED": [True, False]}
    default_options = "shared=False", "NO_GUI=True", "LOGGING_DISABLED=False"
    generators = "cmake"
    requires = "qt/5.12.3@appimage-conan-community/stable"
    build_requires = "cmake_installer/3.14.3@conan/stable"

    def source(self):
        self.run("git clone https://github.com/antony-jr/AppImageUpdaterBridge.git -b v%s" % self.version)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options["shared"]
        cmake.definitions["NO_GUI"] = self.options["NO_GUI"]
        cmake.definitions["LOGGING_DISABLED"] = self.options["LOGGING_DISABLED"]
        cmake.configure(source_folder="AppImageUpdaterBridge")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ["include/AppImageUpdaterBridge"]
        self.cpp_info.libs = ["AppImageUpdaterBridge"]
        self.cpp_info.builddirs = ["lib/cmake"]
