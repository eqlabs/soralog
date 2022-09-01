from conans import ConanFile, CMake

class SoralogConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = "fmt/6.1.2", "yaml-cpp/0.7.0"
   generators = "cmake"

   def build(self):
      cmake = CMake(self)
      cmake.definitions["PACKAGE_MANAGER"] = "Conan"
      cmake.configure()
      cmake.build()
