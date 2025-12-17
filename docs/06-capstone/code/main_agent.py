# main_agent.py
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Mocking VLA Import (In real project, organize as a package)
import sys
sys.path.append("../05-vla-integration/code") 
try:
    from vla_client import VLAClient
except ImportError:
    class VLAClient:
        def analyze_scene(self, img, cmd):
            return {"action": "MOVE", "target": "cube"}

class PhysicalAIAgent(Node):
    def __init__(self):
        super().__init__('physical_ai_agent')
        self.publisher_ = self.create_publisher(String, 'robot_commands', 10)
        self.vla = VLAClient()

    def run_mission(self, user_prompt):
        self.get_logger().info(f"🧠 Processing Prompt: {user_prompt}")
        
        # 1. Perception (Mocking Camera Capture)
        image_path = "latest_frame.jpg"
        
        # 2. Cognition (VLA)
        plan = self.vla.analyze_scene(image_path, user_prompt)
        
        # 3. Action (ROS 2)
        msg = String()
        msg.data = str(plan)
        self.publisher_.publish(msg)
        self.get_logger().info(f"⚡ Executing Plan: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    agent = PhysicalAIAgent()
    
    # Interactive Loop
    print("--- Physical AI Agent Online ---")
    while True:
        cmd = input("Enter command (or 'q'): ")
        if cmd == 'q': break
        agent.run_mission(cmd)

    agent.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
