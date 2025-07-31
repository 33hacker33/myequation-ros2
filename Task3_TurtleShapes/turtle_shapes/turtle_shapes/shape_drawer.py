import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class TurtleShapes(Node):
    def __init__(self):
        super().__init__('turtle_shapes')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        time.sleep(2)  # wait for turtlesim to start
        self.draw_shapes()

    def move(self, linear, angular, duration):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        end_time = time.time() + duration
        while time.time() < end_time:
            self.publisher.publish(msg)
            time.sleep(0.1)
        self.stop()

    def stop(self):
        self.publisher.publish(Twist())
        time.sleep(0.5)

    def draw_square(self):
        self.get_logger().info("Drawing Square")
        for _ in range(4):
            self.move(2.0, 0.0, 1.0)
            self.move(0.0, math.pi / 2, 1.0)

    def draw_triangle(self):
        self.get_logger().info("Drawing Triangle")
        for _ in range(3):
            self.move(2.0, 0.0, 1.0)
            self.move(0.0, 2.1, 1.0)

    def draw_star(self):
        self.get_logger().info("Drawing 5-point Star")
        for _ in range(5):
            self.move(2.0, 0.0, 1.0)
            self.move(0.0, 4 * math.pi / 5, 1.0)

    def draw_shapes(self):
        self.draw_square()
        time.sleep(1)
        self.draw_triangle()
        time.sleep(1)
        self.draw_star()
        self.get_logger().info("Finished drawing all shapes")

def main(args=None):
    rclpy.init(args=args)
    node = TurtleShapes()
    rclpy.spin(node)
    rclpy.shutdown()
