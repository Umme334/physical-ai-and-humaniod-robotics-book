# ros2_bridge.py
from omni.isaac.kit import SimulationApp

# Enable ROS 2 Bridge extension
simulation_app = SimulationApp({
    "headless": False,
    "exts": ["omni.isaac.ros2_bridge"]
})

import omni.graph.core as og
from omni.isaac.core import World
from omni.isaac.core.utils.stage import get_current_stage

def create_ros2_bridge():
    # Create Action Graph for ROS 2
    try:
        og.Controller.edit(
            {"graph_path": "/ActionGraph", "evaluator_name": "execution"},
            {
                "keys": [
                    ("OnPlaybackTick", "omni.graph.action.OnPlaybackTick"),
                    ("ROS2Context", "omni.isaac.ros2_bridge.ROS2Context"),
                    ("ROS2Clock", "omni.isaac.ros2_bridge.ROS2PublishClock"),
                ],
                "connects": [
                    ("OnPlaybackTick.outputs:tick", "ROS2Clock.inputs:execIn"),
                    ("ROS2Context.outputs:context", "ROS2Clock.inputs:context"),
                ],
            },
        )
        print("✅ ROS 2 Bridge Graph Created")
    except Exception as e:
        print(f"❌ Failed to create bridge: {e}")

def main():
    world = World()
    create_ros2_bridge()
    world.reset()

    while simulation_app.is_running():
        world.step(render=True)

    simulation_app.close()

if __name__ == "__main__":
    main()
