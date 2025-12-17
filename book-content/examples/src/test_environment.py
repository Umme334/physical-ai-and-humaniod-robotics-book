import unittest
import sys
import importlib.util

class TestBookEnvironment(unittest.TestCase):
    def test_python_version(self):
        """Ensure Python is 3.8+ for ROS 2 compatibility."""
        self.assertTrue(sys.version_info >= (3, 8), "Python version must be >= 3.8")

    def test_ros2_package_structure(self):
        """Verify basic ROS 2 package structure exists."""
        import os
        base_path = os.path.dirname(os.path.abspath(__file__))
        packages = ['my_robot_control', 'my_robot_description']
        for pkg in packages:
            pkg_path = os.path.join(base_path, pkg)
            self.assertTrue(os.path.isdir(pkg_path), f"Package directory {pkg} missing")

if __name__ == '__main__':
    unittest.main()
