cmake_minimum_required(VERSION 3.0.0)
project(pycall VERSION 0.1.0)

include_directories(
    ${PROJECT_SOURCE_DIR}/include
    /usr/include/python3.8
)

SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

add_executable(pycall ${PROJECT_SOURCE_DIR}/source/main.cc)

target_link_libraries(pycall python3.8)

