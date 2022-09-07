from conans import ConanFile, CMake, tools

class SoralogConan(ConanFile):
   name = "soralog"
   version = "0.0.7"
   settings = "os", "compiler", "build_type", "arch"
   requires = "fmt/6.1.2", "yaml-cpp/0.7.0"
   generators = "cmake"
   # We don't use '/' after '..' as a workaround for
   # https://github.com/conan-io/conan/issues/2675 issue
   exports_sources = "../CMakeLists.txt", "../cmake*", "../example*", "../include*", "../src*", "../test*"

   def build(self):
      cmake = self._configure_cmake()
      cmake.build()

   def package(self):
      cmake = self._configure_cmake()
      cmake.install()

   def _configure_cmake(self):
      cmake = CMake(self)
      cmake.definitions["PACKAGE_MANAGER"] = "Conan"
      cmake.configure()
      return cmake

   def package_info(self):
      self.cpp_info.libdirs = ["lib/soralog"]
      self.cpp_info.libs = tools.collect_libs(self)
