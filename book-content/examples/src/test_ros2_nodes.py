import unittest
import sys
import os

# Add the src directory to the path so we can import the modules
sys.path.append(os.path.join(os.path.dirname(__file__), "my_robot_control"))

class TestROS2Nodes(unittest.TestCase):
    def test_imports(self):
        """Test that we can import the ROS 2 node classes (syntax check + dependency check)."""
        try:
            # We mock rclpy because we might not be in a full ROS 2 environment
            import sys
            from unittest.mock import MagicMock
            sys.modules["rclpy"] = MagicMock()
            sys.modules["rclpy.node"] = MagicMock()
            sys.modules["std_msgs.msg"] = MagicMock()

            from my_robot_control.talker import MinimalPublisher
            from my_robot_control.listener import MinimalSubscriber
            
            self.assertTrue(True, "Successfully imported node classes")
        except ImportError as e:
            self.fail(f"Failed to import ROS 2 nodes: {e}")

if __name__ == '__main__':
    unittest.main()
