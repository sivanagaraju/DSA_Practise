# Kafka Cluster Controller and ZooKeeper Mindmap

## Introduction

- **Kafka as a Masterless Cluster**
  - Kafka does not follow a master-slave architecture.
  - The list of active brokers is maintained in **ZooKeeper**.
- **Need for Administrative Coordination**
  - Routine administrative activities are necessary:
    - Monitoring the list of active brokers.
    - Reassigning work when an active broker leaves the cluster.

## The Controller in Kafka Cluster

- **Definition**
  - A **controller** is a broker elected to take on extra responsibilities.
  - It is **not a master node**.
- **Dual Role**
  - The controller also acts as a **regular broker**.
  - In a single-node cluster, the broker serves both as a controller and a broker.
- **Singleton Property**
  - There is **only one controller** in the Kafka cluster at any point in time.

## Responsibilities of the Controller

- **Monitoring Active Brokers**
  - Monitors the list of active brokers in ZooKeeper.
- **Handling Broker Failures**
  - When a broker leaves the cluster:
    - The controller detects the change via ZooKeeper.
    - It reassigns the work of the departed broker to other active brokers.

## Controller Election Process

- **Initial Election**
  - The **first broker** that starts in the cluster becomes the controller.
    - It creates an **ephemeral controller node** in ZooKeeper.
- **Behavior of Other Brokers**
  - When other brokers start:
    - They attempt to create the controller node.
    - Receive an exception because the node already exists.
    - Realize a controller is already elected.
    - Begin watching the controller node in ZooKeeper for changes.
- **Controller Failure and Re-election**
  - If the controller dies:
    - The ephemeral controller node disappears from ZooKeeper.
    - All brokers detect the disappearance.
    - Each broker tries to create the controller node.
    - **Only one broker succeeds** and becomes the new controller.
    - Others receive an exception and recognize the new controller.
- **Ensuring a Single Controller**
  - This process guarantees:
    - There is **always** a controller.
    - There is **only one** controller at any given time.

## Demonstration Example

- **Setup**
  - A three-node Kafka cluster.
- **Viewing the Controller Node**
  - Use ZooKeeper shell to list the root directory:
    ```bash
    ls /
    ```
  - Observe the presence of the `controller` node.
- **Identifying the Controller**
  - Query the controller node to find out which broker is the controller:
    ```bash
    get /controller
    ```
  - Example output shows `broker id 0` is the controller.
- **Simulating Controller Failure**
  - Stop the broker that is currently the controller (`broker id 0`).
  - Query the controller node again:
    - A new broker is elected as the controller.
- **Restarting the Original Controller Broker**
  - Start `broker id 0` again.
  - Observe that:
    - The broker does **not** regain the controller role.
    - The new controller remains active.
- **Conclusion from Demonstration**
  - Once a new controller is elected, it remains until it fails.
  - Returning brokers do not automatically become the controller.

## Summary

- **ZooKeeper's Role**
  - Acts as the **database** for Kafka cluster control information.
- **Controller's Role**
  - One broker is elected to handle cluster-level activities.
  - Manages broker membership and task reassignment.
- **Cluster Maintenance**
  - The controller ensures smooth operation of the cluster.
  - Maintains high availability by promptly reassigning work upon broker failures.

## Closing Remarks

- **Understanding Kafka Cluster Management**
  - Recognizing the importance of the controller in maintaining cluster integrity.
  - Knowing how the controller is elected and how it functions within the cluster.
- **Encouragement**
  - **Keep learning and keep growing.**

---