import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Node1Publisher(Node):
    def __init__(self):
        super().__init__('node1')
        self.publisher_ = self.create_publisher(String, 'topic1', 10)
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = 'Hello!'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Node1 publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Node1Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
