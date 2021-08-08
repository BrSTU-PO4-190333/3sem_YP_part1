cmake_minimum_required(
    VERSION 3.13
    FATAL_ERROR
)

add_executable(
    main
    src/main.cpp
    src/main.cpp
    src/MyMathOperators/MyMathOperators.cpp
    src/MyMathOperators/MyMathOperators.hpp
    src/MyMathOperators/MyCos/MyCos.cpp
    src/MyMathOperators/MyCos/MyCos.hpp
    src/MyMathOperators/MySin/MySin.cpp
    src/MyMathOperators/MySin/MySin.hpp
    src/MyMathOperators/MyTan/MyTan.cpp
    src/MyMathOperators/MyTan/MyTan.hpp
)

target_link_libraries(
    main
)