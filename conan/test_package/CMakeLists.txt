cmake_minimum_required(VERSION 3.12)

project(PackageTest CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(soralog CONFIG REQUIRED)

add_executable(example main.cpp logging_object.cpp)
target_link_libraries(example soralog::soralog soralog::fallback_configurator)
