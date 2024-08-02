from conan import ConanFile
from conan.tools.files import copy
import os

class RaptorMissionExecutorConan(ConanFile):
  name = "publisher"
  version = "0.0.1"
  user = "sample"
  license = "MIT"
  author = "Chris Sconyers <48865772+chrissconyers@users.noreply.github.com>"
  description = "ros2_transitive_interfaces sample publisher"

  topics = {"sample", "ros2"}
  settings = "os", "compiler", "build_type", "arch"
  options = {"shared": [True, False], "fPIC": [True, False]}
  default_options = {"shared": True, "fPIC": True}

  exports_sources = "src/*", "CMakeLists.txt", "package.xml"
  
  def requirements(self):
    self.requires('interfaces/0.0.1@sample')

  def config_options(self):
    if self.settings.os == "Windows":
      del self.options.fPIC

  def build(self):
    self.run('colcon build')

  def package(self):
    copy(self, "*", dst=self.package_folder, src=os.path.join(self.build_folder, "install"))

  def package_info(self):
    self.buildenv_info.append_path("AMENT_PREFIX_PATH", os.path.join(self.package_folder, self.name))
    self.buildenv_info.append_path("CMAKE_PREFIX_PATH", os.path.join(self.package_folder, self.name))
    self.buildenv_info.append_path("COLCON_PREFIX_PATH", os.path.join(self.package_folder))
    self.buildenv_info.append_path("LD_LIBRARY_PATH", os.path.join(self.package_folder, self.name, "lib"))
    self.buildenv_info.append_path("PYTHONPATH", os.path.join(self.package_folder, self.name, "lib", "python3.8", "site-packages", self.name))
    self.runenv_info.append_path("AMENT_PREFIX_PATH", os.path.join(self.package_folder, self.name))
    self.runenv_info.append_path("CMAKE_PREFIX_PATH", os.path.join(self.package_folder, self.name))
    self.runenv_info.append_path("COLCON_PREFIX_PATH", os.path.join(self.package_folder))
    self.runenv_info.append_path("LD_LIBRARY_PATH", os.path.join(self.package_folder, self.name, "lib"))
    self.runenv_info.append_path("PYTHONPATH", os.path.join(self.package_folder, self.name, "lib", "python3.8", "site-packages", self.name))
