# ros2_transitive_interfaces

Sample repo for re-packaging individual inter-dependent ROS2 packages using Conan.

## workspaces

* `interfaces`: message IDL that defines `Sample` message
  * depends on `std_msgs`
* `publisher`: `Publisher` node packaged as a shared library
  * depends on `interfaces`
* `publisher_node`: executable runs an instance of a `Publisher` node
  * depends on `publisher`

## build using colcon (for testing)

Each step is independent and can be performed in a new session.

1. Build `interfaces`
```
cd interfaces && colcon build
```

2. Build `publisher`
```
cd publisher && . ../interfaces/install/setup.bash && colcon build
```

3. Build `publisher_node`
```
cd publisher_node && . ../publisher/install/setup.bash && colcon build
```

## create conan packages

1. Create `interfaces` package
```
conan create -s compiler.libcxx=libstdc++11 ./interfaces
```

2. Create `publisher` package
```
conan create -s compiler.libcxx=libstdc++11 ./publisher
```

3. Create `publisher_node` package
```
conan create -s compiler.libcxx=libstdc++11 ./publisher_node
```

## deploy
This uses conan's deploy generator as a convenience to expose the package `setup.bash` script.
```
conan install -if install -g deploy publisher_node/0.0.1@
```

## run
```
. install/publisher_node/setup.bash && ros2 run publisher_node publisher_node
```

## license

[MIT License](LICENSE).