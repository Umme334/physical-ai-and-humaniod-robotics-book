from setuptools import setup

package_name = 'my_robot_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Author',
    maintainer_email='author@example.com',
    description='Beginner ROS 2 examples',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_robot_control.talker:main',
            'listener = my_robot_control.listener:main',
        ],
    },
)
