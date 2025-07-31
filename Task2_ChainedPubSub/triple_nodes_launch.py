from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='custom_pub_sub', executable='node1', output='screen'),
        Node(package='custom_pub_sub', executable='node2', output='screen'),
        Node(package='custom_pub_sub', executable='node3', output='screen'),
    ])
