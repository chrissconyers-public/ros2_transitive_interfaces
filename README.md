# ros2_transitive_interfaces

Sample repo for re-packaging individual inter-dependent ROS2 packages using Conan2.

## workspaces

* `interfaces`: message IDL that defines `Sample` message
  * depends on `std_msgs`
* `interfaces_ext`: message IDL that defines `SampleExt` message that embeds a `Sample` message
  * depends on `interfaces`
* `publisher`: `Publisher` node packaged as a shared library
  * publishes `/publisher/hb`, `/publisher/sample`, and `/publisher/sample_ext` topics
  * depends on `interfaces_ext`
* `publisher_node`: executable runs an instance of a `Publisher` node
  * depends on `publisher`

## build using colcon (for testing)

Each step is independent and can be performed in a new session.

1. Build `interfaces`
```
cd interfaces && colcon build
```

2. Build `interfaces_ext`
```
cd interfaces_ext && . ../interfaces/install/setup.bash && colcon build
```

3. Build `publisher`
```
cd publisher && . ../interfaces_ext/install/setup.bash && colcon build
```

4. Build `publisher_node`
```
cd publisher_node && . ../publisher/install/setup.bash && colcon build
```

## create conan packages

1. Create `interfaces` package
```
conan create interfaces/
```

2. Create `interfaces_ext` package
```
conan create interfaces_ext/
```

3. Create `publisher` package
```
conan create publisher/
```

4. Create `publisher_node` package
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
ros2 topic echo /publisher/sample_ext
ros2 topic echo /publisher/hb
```

## license

[MIT License](LICENSE).