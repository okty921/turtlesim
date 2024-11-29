#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

 
 
class TwistJoyNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("twist_joy_node") # MODIFY NAME

        self.robot_name_ = "C3PO"
        self.twist_pub_= self.create_publisher(Twist,"turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):

        class JoySubscriber(Node): # MODIFY NAME
            def __init__(self):
                super().__init__("joy_subscriber_node") # MODIFY NAME
                self.joy_sub_ = self.create_subscription(Joy,"joy", self.joy_sub_callback, 10)

            def joy_sub_callback(self,joy_msg):
                #self.get_logger().info("Sunbcribed message from_node")
                joy_axes = joy_msg.axes
                self.get_logger().info("Axes[0]: %s, Axes[1]: %s" % (str(joy_axes[0]), str(joy_axes[1])))


                #self.get_logger().info("Hello from timer_callback")
                twist_msg = Twist()
                twist_msg.linear.x = str(joy_axes[0])
                twist_msg.angular.z = str(joy_axes[1])
                self.twist_pub_.publish(twist_msg)

        
    

 
 
def main(args=None):
    rclpy.init(args=args)
    node = TwistJoyNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()