#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


class TwistJoyNode(Node):
    def __init__(self):
        super().__init__("twist_joy_node")
        self.robot_name_ = "C3PO" 
        self.twist_pub_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.joy_sub_ = self.create_subscription(Joy, "joy", self.joy_sub_callback, 10)

    def joy_sub_callback(self, joy_msg):
        joy_axes = joy_msg.axes
        self.get_logger().info("Axes[0]: %s, Axes[1]: %s" % (joy_axes[0], joy_axes[1]))

        twist_msg = Twist()
        twist_msg.linear.x = joy_axes[1]    
        twist_msg.angular.z = joy_axes[0]   
        self.twist_pub_.publish(twist_msg)  


def main(args=None):
    rclpy.init(args=args)
    node = TwistJoyNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
