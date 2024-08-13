cmake_minimum_required(VERSION 3.20)
project(publisher VERSION 0.0.1)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(interfaces_ext REQUIRED)

add_library(${PROJECT_NAME} SHARED
  src/publisher.cpp
)
target_include_directories(${PROJECT_NAME}
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/src>
    $<INSTALL_INTERFACE:include>
)
ament_target_dependencies(${PROJECT_NAME}
  rclcpp
  interfaces_ext
)

ament_export_targets(
  export_${PROJECT_NAME}
  HAS_LIBRARY_TARGET
)
ament_export_dependencies(
  rclcpp
  interfaces_ext
)

install(
  TARGETS publisher
  EXPORT export_${PROJECT_NAME}
  DESTINATION lib
  INCLUDES include
)
install (
  FILES src/publisher.hpp
  DESTINATION include
)

ament_package()
