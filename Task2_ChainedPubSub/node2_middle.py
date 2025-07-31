import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Node2Middle(Node):
    def __init__(self):
        super().__init__('node2')
        self.subscription = self.create_subscription(String, 'topic1', self.callback, 10)
        self.publisher_ = self.create_publisher(String, 'topic2', 10)

    def callback(self, msg):
        self.get_logger().info(f'Node2 received: "{msg.data}"')
        response = String()
        response.data = "Hi!"
        self.publisher_.publish(response)
        self.get_logger().info(f'Node2 publishing: "{response.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Node2Middle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
