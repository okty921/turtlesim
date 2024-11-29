#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
 
class joy2TwistNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("joy2twist_node") # MODIFY NAME
        self.get_logger().info("joy2twist_node has been started!")
        self.joy_sub_ = self.create_subscription(Joy, "joy", self.joy_sub_callback,10)
        self.twist_pub_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)

    def joy_sub_callback(self, joy_msg):

        joy_axes = joy_msg.axes
        twist_msg = Twist()
        twist_msg.linear.x = joy_axes[1] * 5
        twist_msg.angular.z = joy_axes[0] * 5
        self.twist_pub_.publish(twist_msg)
 
def main(args=None):
    rclpy.init(args=args)
    node = joy2TwistNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()