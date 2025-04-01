#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
import time

class Balloon(Node):
    def __init__(self):
        super().__init__('stretch_marker')
        self.publisher_ = self.create_publisher(Marker, 'balloon', 10)  

        self.marker = Marker()
        self.marker.header.frame_id = 'map'
        self.marker.header.stamp = self.get_clock().now().to_msg()
        self.marker.type = self.marker.TEXT_VIEW_FACING
        self.marker.id = 0
        self.marker.action = self.marker.ADD
        self.marker.scale.x = 0.5
        self.marker.scale.y = 0.5
        self.marker.scale.z = 0.5
        self.marker.color.r = 1.0
        self.marker.color.g = 0.0
        self.marker.color.b = 0.0
        self.marker.color.a = 1.0
        self.marker.pose.position.x = 5.0
        self.marker.pose.position.y = -6.0
        self.marker.pose.position.z = 0.5
        self.marker.pose.orientation.x = 0.0
        self.marker.pose.orientation.y = 0.0
        self.marker.pose.orientation.z = 0.0
        self.marker.pose.orientation.w = 1.0
        self.marker.text = "0"
        self.get_logger().info("Publishing the balloon topic. Use RViz to visualize.")
    def publish_marker(self):
        self.publisher_.publish(self.marker)
def main(args=None):
    rclpy.init(args=args)
    balloon = Balloon()
    counter = 0
    while rclpy.ok():
        balloon.marker.text = str(counter)
        balloon.publish_marker()
        time.sleep(0.1)
        counter += 1
    balloon.destroy_node()  
    rclpy.shutdown()
if __name__ == '__main__':
    main()