cmake_minimum_required(VERSION 3.15)
project(slambox LANGUAGES C CXX)

SET(CMAKE_CXX_STANDARD 17)
SET(CMAKE_CXX_STANDARD_REQUIRED ON)
SET(CMAKE_CXX_EXTENSIONS NO)

# Gather all source files
file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS 
    ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp
)

# Gather all header files recursively from include
file(GLOB_RECURSE HEADER_FILES CONFIGURE_DEPENDS 
    ${CMAKE_CURRENT_SOURCE_DIR}/include/*.h
    ${CMAKE_CURRENT_SOURCE_DIR}/include/*.hpp
)

# Create the library target
add_library(${PROJECT_NAME} ${SRC_FILES} ${HEADER_FILES})

# Include directories
target_include_directories(${PROJECT_NAME} 
    PUBLIC 
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)


# Dependencies
find_package(Boost REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(GTSAM CONFIG REQUIRED)
find_package(OpenCV REQUIRED)
find_package(TBB REQUIRED)
find_package(symforce REQUIRED CONFIG)

target_link_libraries(${PROJECT_NAME}
    PRIVATE
        Boost::boost
        Eigen3::Eigen
        ${GTSAM_LIBRARIES}
        ${OpenCV_LIBS}
        TBB::tbb
        symforce::symforce
)

# Compiler-specific flags
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    target_compile_options(${PROJECT_NAME} PUBLIC 
        "$<$<CONFIG:Debug>:-Wall;-Wextra;-Werror;-pedantic;-ggdb;-O0>"
        "$<$<CONFIG:Release>:-Wall;-Wextra;-Werror;-pedantic;-O3>"
    )
endif()

# Main executable
add_executable(main src/main.cpp)
target_link_libraries(main PRIVATE ${PROJECT_NAME})

# Optional tests
if(NOT BUILD_TESTING STREQUAL OFF)
    add_subdirectory(tests)
endif()
