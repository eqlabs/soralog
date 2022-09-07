cmake_minimum_required(VERSION 3.12)

project(PackageTest CXX)

find_package(soralog CONFIG REQUIRED)

add_executable(example main.cpp)
target_link_libraries(example soralog::soralog)
