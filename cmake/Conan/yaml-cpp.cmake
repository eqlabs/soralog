add_conan_package(yaml-cpp 0.7.0)
find_package(yaml-cpp MODULE REQUIRED)
include_directories(${yaml-cpp_INCLUDE_DIRS})
