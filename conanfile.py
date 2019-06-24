from conans import ConanFile, CMake, tools


class AppImageUpdaterBridgeConan(ConanFile):
    name = "AppImageUpdaterBridge"
    version = "1.0.4"
    license = "MIT"
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

    def package(self):
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

        tools.replace_in_file("AppImageUpdaterBridge/AppImageUpdaterBridge", 'include/', '')
        self.copy("AppImageUpdaterBridge", dst="include", src="AppImageUpdaterBridge", keep_path=False)
        self.copy("appimageupdaterbridge.hpp", dst="include", src="AppImageUpdaterBridge/include", keep_path=False)
        self.copy("appimagedeltarevisioner.hpp", dst="include", src="AppImageUpdaterBridge/include", keep_path=False)
        self.copy("appimageupdaterbridge_enums.hpp", dst="include", src="AppImageUpdaterBridge/include",
                  keep_path=False)

        if not self.options["NO_GUI"]:
            tools.replace_in_file("AppImageUpdaterBridge/AppImageUpdaterDialog", 'include/', '')
            self.copy("AppImageUpdaterDialog", dst="include", src="AppImageUpdaterBridge", keep_path=False)
            self.copy("appimageupdaterdialog.hpp", dst="include", src="AppImageUpdaterBridge/include", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["AppImageUpdaterBridge"]
