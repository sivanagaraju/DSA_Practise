# Responsibilities of Leaders and Followers in Kafka Brokers Mindmap

## Introduction

- **Context**
  - Previous session: Learned how replicas are distributed among brokers in the cluster.
  - Current lecture: Discussing the responsibilities of the leader and the followers.

## Brokers and Partition Types

- **Brokers Manage Two Types of Partitions**
  1. **Leader Partitions**
  2. **Follower Partitions**
- **Broker Activities Depend on Partition Type**
  - **Leader Activities**
  - **Follower Activities**

## Example Scenario

- **Cluster Setup**
  - **Total Replicas**: 30 replicas among 6 brokers.
  - **Broker 4**:
    - Holds 6 replicas:
      - **2 Leader Partitions**
      - **4 Follower Partitions**
- **Roles of Broker 4**
  - Acts as a leader for 2 leader partitions.
  - Acts as a follower for 4 follower partitions.

## Leader Broker Responsibilities

- **Definition of Leader Broker**
  - Responsible for all requests from producers and consumers.
- **Producer Interaction**
  - **Producer Connection**
    - Producer connects to any broker in the cluster.
    - Queries for topic metadata.
  - **Metadata Response**
    - All Kafka brokers can answer metadata requests.
    - Metadata contains a list of all leader partitions and their respective host and port information.
  - **Producer Decision**
    - Producer decides which partition to send data to.
    - Sends the message directly to the leader of that partition.
  - **Leader's Action**
    - Leader broker persists the message in the leader partition.
    - Sends back an acknowledgement to the producer.
- **Consumer Interaction**
  - Consumers always read messages from the leader of the partition.
- **Summary of Leader Responsibilities**
  - Interact with producers and consumers.
  - Handle all read and write requests for their partitions.

## Follower Broker Responsibilities

- **Definition of Follower Broker**
  - Brokers that hold follower partitions allocated to them.
- **Follower Activities**
  - Do not serve producer and consumer requests.
  - Only job is to copy messages from the leader.
  - Aim to stay up-to-date with all messages.
- **Goal of Followers**
  - To get elected as a leader if the current leader fails or dies.
  - Must stay in-sync with the leader to be eligible for leadership.
- **Staying In-Sync with the Leader**
  - **Process**
    - Follower connects to the leader.
    - Requests data (messages) from the leader.
    - Leader sends messages to the follower.
    - Follower persists the messages into its replica.
    - Follower requests more data in a continuous loop.
  - **Continuous Process**
    - This goes on forever as an infinite loop.
    - Ensures followers are always up-to-date with the leader.
- **Importance of Staying In-Sync**
  - Followers cannot get elected as leaders if they are falling behind.
  - Must have up-to-date data to take over leadership if needed.

## Conclusion

- **Summary**
  - Brokers perform different activities based on whether they are leaders or followers.
  - **Leaders** handle all producer and consumer requests.
  - **Followers** replicate data from leaders to stay in-sync.
- **Closing Remarks**
  - "Great, see you again. Keep learning and keep growing."

---

**Note:** This mindmap captures all the key concepts and details from the lecture, ensuring that every piece of information is included and organized logically for a comprehensive understanding.