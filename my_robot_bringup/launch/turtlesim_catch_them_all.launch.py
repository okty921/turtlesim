from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    ld = LaunchDescription()

    config_file_path = os.path.join(
        "turtlesim_catch_them_all"
        "config",
        "turtlesim_catch_them_all_config.yaml"
    )

    turtlesim_node = Node(
        package="turtlesim",
        executable="turtlesim_node"
    )

    turtle_spawner_node = Node(
        package="turtlesim_catch_them_all",
        executable="turtle_spawner",
        parameters=[config_file_path]
    )

    turtle_controller_node = Node(
        package="turtlesim_catch_them_all",
        executable="turtlesim_controller",
        parameters=[config_file_path]
    )

    ld.add_action(turtlesim_node)
    ld.add_action(turtle_spawner_node)
    ld.add_action(turtle_controller_node)
    return ld