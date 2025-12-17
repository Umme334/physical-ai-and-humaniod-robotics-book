# load_robot.py
from omni.isaac.kit import SimulationApp

# 1. Start the Simulator
simulation_app = SimulationApp({"headless": False})

from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
from omni.isaac.core.utils.types import ArticulationAction
import numpy as np

def main():
    # 2. Create the World
    world = World()
    world.scene.add_default_ground_plane()

    # 3. Add a Robot (Dynamic Cube for simplicity)
    robot = world.scene.add(
        DynamicCuboid(
            prim_path="/World/MyRobot",
            name="simple_robot",
            position=np.array([0, 0, 1.0]),
            scale=np.array([0.5, 0.5, 0.5]),
            color=np.array([0, 0, 1.0]),
        )
    )

    world.reset()

    # 4. Simulation Loop
    while simulation_app.is_running():
        world.step(render=True)
        
        # Example: Apply force or move
        # robot.apply_action(...)

    simulation_app.close()

if __name__ == "__main__":
    main()
