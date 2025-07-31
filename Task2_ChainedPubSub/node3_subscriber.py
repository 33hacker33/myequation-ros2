import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Node3Subscriber(Node):
    def __init__(self):
        super().__init__('node3')
        self.subscription = self.create_subscription(String, 'topic2', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'Node3 received: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Node3Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
