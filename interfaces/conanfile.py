from conans import ConanFile, CMake, tools
import os

class RaptorMissionExecutorConan(ConanFile):
  name = "interfaces"
  version = "0.0.1"
  exports_sources = "msg/*", "CMakeLists.txt", "package.xml"
  license = "MIT"
  author = "Chris Sconyers <48865772+chrissconyers@users.noreply.github.com>"
  description = "ros2_transitive_interfaces sample interfaces"
  settings = "os", "compiler", "build_type", "arch"
  options = {"shared": [True, False], "fPIC": [True, False]}
  default_options = {"shared": True, "fPIC": True}
  generators = "cmake_find_package", "cmake_paths"
  _cmake = None

  def configure(self):
    if self.settings.compiler.libcxx == "libstdc++":
      raise Exception("This package is only compatible with libstdc++11")

  def config_options(self):
    if self.settings.os == "Windows":
      del self.options.fPIC

  def build(self):
    self.run('colcon build')

  def package(self):
    self.copy("*", dst=self.package_folder, src=os.path.join(self.build_folder, "install"))

  def package_info(self):
    self.env_info.AMENT_PREFIX_PATH.append(self.package_folder)
    self.env_info.CMAKE_PREFIX_PATH.append(self.package_folder)
    self.env_info.COLCON_PREFIX_PATH.append(self.package_folder)
    self.env_info.LD_LIBRARY_PATH.append(os.path.join(self.package_folder, "lib", self.name))
    self.env_info.PYTHONPATH.append(os.path.join(self.package_folder, "lib", "python3.8", "site-packages", self.name))
  