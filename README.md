# ros2_transitive_interfaces

Sample repo for re-packaging individual inter-dependent ROS2 packages using Conan2.

## workspaces

* `interfaces`: message IDL that defines `Sample` message
  * depends on `std_msgs`
* `publisher`: `Publisher` node packaged as a shared library
  * publishes `/publisher/hb` and `/publisher/sample` topics
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
conan create interfaces/
```

2. Create `publisher` package
```
conan create publisher/
```

3. Create `publisher_node` package
```
conan create publisher_node/
```

## deploy
```
conan install -d full_deploy -of install .
```

## run
```
. install/conanrun.sh && ros2 run publisher_node publisher_node
```

## verify messages and interfaces
```
. install/conanrun.sh
ros2 topic echo /publisher/sample
ros2 topic echo /publisher/hb
```

## license

[MIT License](LICENSE).