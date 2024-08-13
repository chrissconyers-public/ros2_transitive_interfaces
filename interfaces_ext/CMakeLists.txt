cmake_minimum_required(VERSION 3.20)
project(interfaces_ext VERSION 0.0.1)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(interfaces REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/SampleExt.msg"
  DEPENDENCIES
    interfaces
)

ament_export_dependencies(
  interfaces
)

ament_package()
