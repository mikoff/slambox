cmake_minimum_required(VERSION 3.15)
project(SlamboxTest CXX)

find_package(GTest REQUIRED CONFIG)
find_package(TBB REQUIRED)

add_executable(dummy_test dummy_test.cpp)
target_link_libraries(dummy_test GTest::gtest GTest::gtest_main slambox TBB::tbb)
