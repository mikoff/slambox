cmake_minimum_required(VERSION 3.15)
project(slambox C CXX)

add_library(${PROJECT_NAME} src/slam.cpp)
target_include_directories(${PROJECT_NAME} PUBLIC include)
set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER "include/slam.h")

find_package(Boost REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(GTSAM REQUIRED)
find_package(OpenCV REQUIRED)

include_directories(${Boost_INCLUDE_DIRS})
include_directories(${Eigen_INCLUDE_DIRS})
include_directories(${GTSAM_INCLUDE_DIR})
include_directories(${OpenCV_INCLUDE_DIRS})

target_link_libraries(${PROJECT_NAME}
    ${Boost_LIBRARIES}
    ${Eigen_LIBRARIES}
    ${GTSAM_LIBRARIES}
    ${OpenCV_LIBS}
    )

if (NOT BUILD_TESTING STREQUAL OFF)
    add_subdirectory(tests)
endif()

if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    set(GCC_COMPILE_OPTIONS "-Wall;-Wextra;-Werror;-pedantic")
    set(GCC_COMPILE_DEBUG_OPTIONS "${GCC_COMPILE_OPTIONS};-ggdb;-O0")
    set(GCC_COMPILE_RELEASE_OPTIONS "${GCC_COMPILE_OPTIONS};-O3")
    target_compile_options(${PROJECT_NAME} PUBLIC "$<$<CONFIG:Debug>:${GCC_COMPILE_DEBUG_OPTIONS}>")
    target_compile_options(${PROJECT_NAME} PUBLIC "$<$<CONFIG:Release>:${GCC_COMPILE_RELEASE_OPTIONS}>")
endif()

add_executable(main src/main.cpp)
add_dependencies(main ${PROJECT_NAME})
target_include_directories(main PUBLIC include)
target_link_libraries(main ${PROJECT_NAME})
