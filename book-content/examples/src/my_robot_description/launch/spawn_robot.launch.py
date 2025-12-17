import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'my_robot_description'
    urdf_file_name = 'robot.urdf'

    urdf = os.path.join(
        get_package_share_directory(package_name),
        'urdf',
        urdf_file_name)
    
    # Read URDF content
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        # Start Gazebo
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        # Publish robot state
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}],
            arguments=[urdf]
        ),

        # Spawn entity
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'simple_bot', '-topic', 'robot_description'],
            output='screen'
        ),
    ])
