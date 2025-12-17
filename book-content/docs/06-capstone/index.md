---
id: capstone
title: Chapter 6: Capstone Integration
sidebar_label: 6. Capstone
---

# Chapter 6: Capstone Integration

It is time to build the full **Physical AI Pipeline**.

## The Architecture

We are connecting all the pieces:
1.  **The Body**: Isaac Sim with a robot.
2.  **The Nervous System**: ROS 2 communication.
3.  **The Mind**: VLA Client script.

![Architecture Diagram](assets/architecture_diagram.mermaid)

## The Main Agent

We need a central ROS 2 node to orchestrate this. This node will:
1.  Listen for user input.
2.  Call the VLA Client.
3.  Publish ROS messages to the robot.

```python
class PhysicalAIAgent(Node):
    def run_mission(self, user_prompt):
        # 1. Perception
        image = self.get_camera_frame()
        
        # 2. Cognition (VLA)
        plan = self.vla.analyze_scene(image, user_prompt)
        
        # 3. Action
        self.publisher_.publish(str(plan))
```

## Running the Capstone

1.  **Start Isaac Sim**: Ensure the bridge is running.
2.  **Start the Agent**: `python main_agent.py`.
3.  **Command**: "Move the blue cube to the left."

### What Happens?
1.  The Agent grabs the frame.
2.  GPT-4o (or similar) analyzes it and outputs `{"action": "MOVE", "target": "blue_cube", "vector": [-1, 0, 0]}`.
3.  The Agent publishes this JSON.
4.  A Controller node (not shown, but implied) moves the cube in Sim.

## Conclusion

You have successfully built a Physical AI system! You moved beyond hard-coded scripts to intent-based control. This is the future of robotics.
