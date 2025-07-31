# MyEquation Internship – ROS 2 Module  
## 🧪 Task 1: Custom Publisher and Subscriber Using Custom Message

This project was completed as part of my internship at **MyEquation**, under the **ROS 2 module**. The task involved implementing basic communication in ROS 2 using a **custom message type**.

---

## 🧠 Task Summary

- Create a custom message type (`Example.msg`)
- Write a **Publisher Node** that publishes the current time with a message
- Write a **Subscriber Node** that receives and prints the message
- Visualize communication using `rqt_graph` and terminal logs

---

## 📂 Project Structure

| File                         | Description                                      |
|------------------------------|--------------------------------------------------|
| `custom_msg_publisher.py`    | Publishes time-based messages to `/my_topic`     |
| `custom_msg_subscriber.py`   | Subscribes to `/my_topic` and logs message       |
| `rqt_graph.jpg`              | Screenshot of working pub-sub connection         |

---

## 💬 Custom Message Definition

Message type used: `Example.msg`  
Location: `part1_pubsub/msg/Example.msg`

```plaintext
string info
int32 time
