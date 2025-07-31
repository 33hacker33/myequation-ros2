#!/usr/bin/env python3
# A simple ROS2 Subscriber

import rclpy
from rclpy.node import Node

from part1_pubsub.msg import Example  # Import the correct message type

class SimpleSubscriber(Node): 

    def __init__(self): 
        super().__init__("simple_subscriber") 

        self.my_subscriber = self.create_subscription(
            msg_type=Example,  # Use the Example message type
            topic="my_topic",  # Subscribe to the same topic
            callback=self.msg_callback,
            qos_profile=10,
        ) 

        self.get_logger().info(
            f"The '{self.get_name()}' node is initialised."
        ) 

    def msg_callback(self, topic_message: Example):  # Modify the callback to expect an Example message
        # Access 'info' and 'time' fields from the Example message
        self.get_logger().info(
            f"\nThe '{self.get_name()}' node heard:\n"
            f"  Info: '{topic_message.info}'\n"
            f"  Time: {topic_message.time}"
        )

def main(args=None): 
    rclpy.init(args=args)
    my_simple_subscriber = SimpleSubscriber()
    rclpy.spin(my_simple_subscriber)
    my_simple_subscriber.destroy_node()
    rclpy.shutdown() 

if __name__ == '__main__': 
    main()
