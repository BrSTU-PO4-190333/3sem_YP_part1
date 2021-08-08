cmake_minimum_required(
    VERSION 3.13
    FATAL_ERROR
)

add_executable(
    main
    src/main.cpp
    src/main.cpp
    src/lib/lib.cpp
    src/lib/lib.hpp
)

target_link_libraries(
    main
)