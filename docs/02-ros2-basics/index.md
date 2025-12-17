---
id: ros2-basics
title: "Chapter 2: The Nervous System (ROS 2)"
sidebar_label: "2. ROS 2 Basics"
---

# Chapter 2: The Nervous System (ROS 2)

In biology, the nervous system transmits signals. In robotics, **ROS 2** (Robot Operating System) does the same. It provides the plumbing for your robot's software components to talk to each other.

## Key Concepts

### 1. Nodes
A **Node** is a process that performs a computation. Think of it as a single brain cell or a specific organ. One node might control a motor, another might process a camera feed.

### 2. Topics
Nodes exchange information over **Topics**. This is a publish-subscribe model:
- **Publisher Node**: "I have new data!" (Sends message to a topic)
- **Subscriber Node**: "I want that data!" (Listens to the topic)

## Hands-On: Your First ROS 2 Network

We have created a package `my_robot_control` with two nodes: a Talker and a Listener.

### The Talker Code (`talker.py`)

```python
class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        # Create a publisher on topic 'topic'
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        # Timer to trigger callback every 0.5 seconds
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World'
        self.publisher_.publish(msg)
```

### The Listener Code (`listener.py`)

```python
class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        # Subscribe to 'topic'
        self.subscription = self.create_subscription(
            String, 'topic', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
```

### Running the Nodes

1.  **Build your workspace**:
    ```bash
    colcon build --packages-select my_robot_control
    source install/setup.bash
    ```

2.  **Run the Talker**:
    ```bash
    ros2 run my_robot_control talker
    ```

3.  **Run the Listener** (in a new terminal):
    ```bash
    ros2 run my_robot_control listener
    ```

You should see the messages passing from one node to the other!
