from conan import ConanFile

class SampleConan(ConanFile):
  settings = "os", "compiler", "build_type", "arch"
  options = {"shared": [True, False], "fPIC": [True, False]}
  default_options = {"shared": True, "fPIC": True}
  generators = "CMakeToolchain", "CMakeDeps"

  def requirements(self):
    self.requires("publisher_node/0.0.1@sample")
