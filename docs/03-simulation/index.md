---
id: simulation
title: "Chapter 3: The Digital Body"
sidebar_label: "3. Simulation"
---

# Chapter 3: The Digital Body

Before we build hardware, we simulate. Simulation allows us to crash our robot a thousand times without costing a dime.

## The Universal Robot Description Format (URDF)

To put a robot in a simulator, we need to describe it using XML. We call this file a **URDF**.

### Anatomy of a Robot

- **Links**: The solid parts (Body, Head, Arm).
- **Joints**: The moving parts connecting links (Hinge, Slider).

### Your First Robot (`robot.urdf`)

We created a simple robot with a box body and a sphere head.

```xml
<robot name="simple_bot">
  <link name="base_link">
    <!-- Visual: What it looks like -->
    <visual>
      <geometry><box size="0.5 0.5 0.2"/></geometry>
    </visual>
    <!-- Collision: Where it hits things -->
    <collision>
      <geometry><box size="0.5 0.5 0.2"/></geometry>
    </collision>
    <!-- Inertial: How heavy it is -->
    <inertial>
       <mass value="5.0"/>
       <!-- Inertia matrix ... -->
    </inertial>
  </link>
  <!-- ... Head link and Joint ... -->
</robot>
```

## Launching in Gazebo

We use a **Launch File** to start the simulator and spawn our robot.

1.  **Build the package**:
    ```bash
    colcon build --packages-select my_robot_description
    source install/setup.bash
    ```

2.  **Launch**:
    ```bash
    ros2 launch my_robot_description spawn_robot.launch.py
    ```

You should see Gazebo open and your blue box robot drop into the world!
