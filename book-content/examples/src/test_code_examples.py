import unittest
import os
import ast
import xml.etree.ElementTree as ET

class TestBookCode(unittest.TestCase):
    def setUp(self):
        # Adjust path to project root relative to this test file
        self.root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
        self.docs_dir = os.path.join(self.root_dir, "book-content", "docs")
        self.examples_dir = os.path.join(self.root_dir, "book-content", "examples", "src")

    def test_urdf_validity(self):
        """Parse the URDF file to ensure valid XML structure."""
        urdf_path = os.path.join(self.examples_dir, "my_robot_description", "urdf", "robot.urdf")
        self.assertTrue(os.path.exists(urdf_path), f"URDF file missing at {urdf_path}")
        
        try:
            tree = ET.parse(urdf_path)
            root = tree.getroot()
            self.assertEqual(root.tag, "robot", "Root element should be <robot>")
            
            # Check for base_link
            links = [link.get('name') for link in root.findall('link')]
            self.assertIn("base_link", links, "URDF missing 'base_link'")
            
        except ET.ParseError as e:
            self.fail(f"URDF XML parsing failed: {e}")

    def test_python_syntax_in_docs(self):
        """Ensure all Python scripts in docs/ folders have valid syntax."""
        python_files = []
        for root, dirs, files in os.walk(self.docs_dir):
            for file in files:
                if file.endswith(".py"):
                    python_files.append(os.path.join(root, file))

        self.assertTrue(len(python_files) > 0, "No Python files found in docs to test")

        for file_path in python_files:
            with self.subTest(file=os.path.basename(file_path)):
                with open(file_path, "r", encoding="utf-8") as f:
                    source = f.read()
                try:
                    ast.parse(source)
                except SyntaxError as e:
                    self.fail(f"Syntax error in {file_path}: {e}")

    def test_ros2_node_files_exist(self):
        """Verify ROS 2 node files exist."""
        control_pkg = os.path.join(self.examples_dir, "my_robot_control", "my_robot_control")
        self.assertTrue(os.path.exists(os.path.join(control_pkg, "talker.py")))
        self.assertTrue(os.path.exists(os.path.join(control_pkg, "listener.py")))

if __name__ == "__main__":
    unittest.main()
