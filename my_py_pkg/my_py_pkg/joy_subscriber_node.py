#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
 
 
class JoySubscriber(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("joy_subscriber_node") # MODIFY NAME
        self.joy_sub_ = self.create_subscription(Joy,"joy", self.joy_sub_callback, 10)

    def joy_sub_callback(self,joy_msg):
        #self.get_logger().info("Sunbcribed message from_node")
        joy_axes = joy_msg.axes
        self.get_logger().info("Axes[0]: %s, Axes[1]: %s" % (str(joy_axes[0]), str(joy_axes[1])))
 
def main(args=None):
    rclpy.init(args=args)
    node = JoySubscriber() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()