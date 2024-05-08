cmake_minimum_required(VERSION 3.20)
project(publisher_node VERSION 0.0.1)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(publisher REQUIRED)

add_executable(${PROJECT_NAME}
  src/publisher_node.cpp
)
ament_target_dependencies(${PROJECT_NAME}
  publisher
)
install(
  TARGETS ${PROJECT_NAME}
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
