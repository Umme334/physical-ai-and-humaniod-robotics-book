---
id: isaac-sim
title: "Chapter 4: The AI Brain"
sidebar_label: "4. Isaac Sim & AI"
---

# Chapter 4: The AI Brain

While Gazebo is great for physics testing, **NVIDIA Isaac Sim** is built for AI. It allows us to train robots using visual data and perform photorealistic simulations.

## Setting Up Isaac Sim

Isaac Sim uses **Omniverse**. It requires a powerful GPU (RTX series).

1.  Install **NVIDIA Omniverse Launcher**.
2.  Install **Isaac Sim** from the Exchange.
3.  Launch the "ROS 2 Bridge" snippet to verify connectivity.

## Loading a Robot via Python

Instead of XML launch files, we often use Python scripts in Isaac Sim.

```python
from omni.isaac.kit import SimulationApp
simulation_app = SimulationApp({"headless": False})
from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
import numpy as np

world = World()
# Add a blue cube representing our robot
robot = world.scene.add(
    DynamicCuboid(
        prim_path="/World/MyRobot",
        name="simple_robot",
        position=np.array([0, 0, 1.0]),
        color=np.array([0, 0, 1.0]),
    )
)

while simulation_app.is_running():
    world.step(render=True)

simulation_app.close()
```

## Bridging to ROS 2

The **ROS 2 Bridge** connects the simulator to your nervous system. In Isaac Sim, this is often done using an **Action Graph**.

When the bridge is running, Isaac Sim becomes just another ROS 2 node. It publishes sensor data (camera, lidar) and subscribes to control commands (velocity, joints).

### Checkpoint
Run `ros2 topic list` while your Isaac Sim script is running. You should see `/clock` being published by the simulator!
