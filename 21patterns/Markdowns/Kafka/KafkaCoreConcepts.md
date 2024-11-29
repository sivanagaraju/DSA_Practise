# Apache Kafka Core Concepts Mindmap

## Introduction
- **Purpose of Lecture**
  - Explain fundamental concepts associated with Kafka.
  - Build clear understanding of terminologies.
  - Foundation for the rest of the training.

## Core Concepts

### Producer
- **Definition**
  - An application that sends data (messages/records) to Kafka.
  - Data is a small to medium-sized piece of data.
  - For Kafka, a message is just an array of bytes.
- **Examples**
  - Sending each line of a data file as a message.
  - Sending each row of a database table as a message.
  - Sending results of a database query as messages.
- **Implementation**
  - Create a producer application to send data.
  - May find out-of-the-box producers for specific purposes.

### Consumer
- **Definition**
  - An application that receives data from Kafka.
  - Consumers are recipients of data sent by producers.
- **Mechanism**
  - Producers send data to Kafka server (broker).
  - Consumers request data from the Kafka server.
  - Producers and consumers do not interact directly.
- **Process**
  - Consumer application requests data from Kafka server.
  - Receives messages, processes them, and requests more.
  - Operates in a loop as long as new messages arrive.
- **Usage**
  - Up to the consumer application to process data (e.g., compute aggregates, send alerts).

### Broker
- **Definition**
  - The Kafka server is called a broker.
- **Role**
  - Acts as a message broker between producers and consumers.
  - Facilitates the exchange of messages.
  - Producers and consumers communicate via the broker.

### Cluster
- **Definition**
  - A group of computers acting together for a common purpose.
- **Kafka Cluster**
  - A group of computers, each running an instance of the Kafka broker.
  - Kafka is a distributed system.
- **Purpose**
  - Enables scalability and fault tolerance.
  - Distributes workload across multiple machines.

### Topic
- **Definition**
  - An arbitrary, unique name given to a data set or data stream.
  - Similar to a database table in concept.
- **Purpose**
  - Organizes data sent by producers and requested by consumers.
  - Helps specify which data a consumer wants.
- **Creation**
  - Creating a topic is a design-time decision.
  - Architects decide on topics during application design.
- **Example (Smart Meter)**
  - Producers send different types of data:
    - **Current-load** (sent every minute).
    - **Consumed-units** (sent every hour).
    - **Input-current-fluctuations** (sent as they happen).
  - Create separate topics for each data type:
    - `current-load` topic.
    - `consumed-units` topic.
    - `input-fluctuations` topic.
- **Communication**
  - Producers send messages to specific topics.
  - Consumers request data from specific topics.
- **Analogy**
  - Think of a topic as a database table where producers insert records and consumers read them.
- **Benefits**
  - Reduces confusion in data retrieval.
  - Simplifies producer and consumer interactions with the broker.

### Partition
- **Definition**
  - A topic is split into multiple smaller parts called partitions.
  - Each partition is an independent portion of the topic.
- **Purpose**
  - Solves storage capacity challenges by distributing data across multiple machines.
  - Enables scalability and parallelism in data handling.
- **Implementation**
  - Partitions are stored on different brokers in the cluster.
- **Design Decision**
  - Number of partitions is specified when creating a topic.
  - Architects decide the number of partitions based on expected data volume.
- **Limitations**
  - A partition resides on a single machine and cannot be broken further.
  - Must estimate partitions meaningfully.
- **Example**
  - `current-load` topic may have 100 partitions (high volume).
  - `consumed-units` topic may have 20 partitions (lower volume).
- **Key Point**
  - Partitions are crucial for both storage capacity and workload distribution.

### Offset
- **Definition**
  - A unique sequential ID assigned to each message within a partition.
  - Assigned by the broker upon message arrival.
- **Properties**
  - Offsets are immutable once assigned.
  - Offsets start from zero and increment by one within each partition.
- **Ordering**
  - Messages within a partition are ordered by their offsets.
  - No global ordering across partitions.
- **Locating a Message**
  - To locate a specific message, you need:
    - Topic name.
    - Partition number.
    - Offset number.
- **Importance**
  - Essential for message retrieval and ensuring message processing order within a partition.

### Consumer Group
- **Definition**
  - A group of consumers that work together to consume data from a topic.
- **Purpose**
  - Allows multiple consumers to share the workload.
  - Enables parallel processing of data.
- **Mechanism**
  - Each consumer in the group reads data from different partitions.
  - Ensures that each partition is consumed by only one consumer in the group.
- **Benefits**
  - Scalability on the consumer side.
  - Efficient handling of large volumes of data.
- **Analogy**
  - Similar to dividing a large task among multiple people to accomplish it faster.

## Comprehensive Example: Retail Chain

### Scenario
- **Context**
  - Retail chain with multiple stores and billing counters.
- **Objective**
  - Bring all invoices from every billing counter to the data center quickly.

### Implementation

#### Producers
- **At Billing Locations**
  - Create a producer at every billing counter.
  - Producers send invoices as messages to a Kafka topic.

#### Kafka Cluster
- **Scaling**
  - Use a large Kafka cluster to handle high volume and velocity.
  - Partition the topic to distribute data.
- **Partitions**
  - Topic partitions help:
    - Increase storage capacity.
    - Distribute workload across brokers.
    - Enhance scalability.

#### Consumers
- **Initial Approach**
  - Create a single consumer to read data from the Kafka topic.
  - Consumer writes data to the data center.
- **Problem Identified**
  - Single consumer cannot handle the high incoming data volume alone.

#### Consumer Group Solution
- **Implementation**
  - Create a consumer group with multiple consumer instances.
  - Start multiple copies of the consumer application in the same group.
- **Work Division**
  - Consumers divide the partitions among themselves.
  - Example:
    - 500 partitions and 100 consumers.
    - Each consumer handles 5 partitions.
- **Scaling Consumers**
  - Can add more consumers if needed.
  - Maximum number of consumers is equal to the number of partitions.
- **Benefits**
  - Efficiently handles large data volumes.
  - Balances the workload among consumers.

### Key Learnings
- **Partitions as a Tool**
  - Partitions enable Kafka to be a distributed and scalable system.
  - They are essential for both storage and workload distribution.
- **Consumer Groups for Scalability**
  - Allow scaling on the consumer side.
  - Ensure efficient data processing.
- **Limitations**
  - Kafka doesn't allow more than one consumer in a group to read from the same partition simultaneously.
  - Necessary to prevent duplicate processing of records.

## Conclusion
- **Summary**
  - Covered critical core concepts of Apache Kafka.
  - Familiarized with key terminologies:
    - Producer
    - Consumer
    - Broker
    - Cluster
    - Topic
    - Partition
    - Offset
    - Consumer Group
- **Emphasis**
  - Understanding these concepts is crucial for working effectively with Kafka.
  - Partitions are the most valuable concept for Kafka's scalability.
- **Next Steps**
  - Further exploration of Kafka's capabilities.
  - Application of these concepts in practical scenarios.
- **Closing Note**
  - Keep learning and keep growing.

---
