cmake_minimum_required(VERSION 3.15)
project(slambox LANGUAGES C CXX)

# Create the library target from src/slam.cpp
add_library(${PROJECT_NAME} src/slam.cpp)
target_include_directories(${PROJECT_NAME} 
    PUBLIC 
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
set_target_properties(${PROJECT_NAME} PROPERTIES
    PUBLIC_HEADER "include/slam.h"
)

# Use Conan-generated config files via find_package() without manually setting CMAKE_MODULE_PATH.
find_package(Boost REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(GTSAM CONFIG REQUIRED)
find_package(OpenCV REQUIRED)
find_package(TBB REQUIRED)
find_package(symforce REQUIRED CONFIG)

# Link libraries using imported targets where available
target_link_libraries(${PROJECT_NAME}
    PRIVATE
        Boost::boost
        Eigen3::Eigen
        ${GTSAM_LIBRARIES}
        ${OpenCV_LIBS}
        TBB::tbb
        symforce::symforce
)

# If tests are enabled, add the tests subdirectory
if(NOT BUILD_TESTING STREQUAL OFF)
    add_subdirectory(tests)
endif()

# Add compiler-specific flags using target_compile_options
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    target_compile_options(${PROJECT_NAME} PUBLIC 
        "$<$<CONFIG:Debug>:-Wall;-Wextra;-Werror;-pedantic;-ggdb;-O0>"
        "$<$<CONFIG:Release>:-Wall;-Wextra;-Werror;-pedantic;-O3>"
    )
endif()

# Create the main executable and link it with the library target
add_executable(main src/main.cpp)
target_link_libraries(main PRIVATE ${PROJECT_NAME})
target_include_directories(main PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
