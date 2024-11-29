#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
 
 
class StringSubscriberNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("string_subscriber_node") # MODIFY NAME
        self.str_sub_ = self.create_subscription(String,"string_message", self.str_sub_callback, 10)

    def str_sub_callback(self,str_msg):
        self.get_logger().info("Hello from string_subscriber_callback_node")
 
def main(args=None):
    rclpy.init(args=args)
    node = StringSubscriberNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()