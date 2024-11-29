# Kafka Consumer Group and Partitions Demo Mindmap

## Introduction

- **Context**
  - Previous lecture: Created a three-node Kafka cluster.
  - Current lecture: Use the three-node Kafka cluster to demonstrate Kafka's partitioning and consumer group features.

- **Objectives**
  - Create a new Kafka topic with three partitions.
  - Start two consumers in the same consumer group reading from the same topic.
  - Observe how the consumers share the workload.
  - Start a producer to send a data file to the Kafka cluster.
  - Examine how data is distributed across partitions and consumed by the consumers.

## Steps Performed

### 1. Ensuring the Kafka Cluster is Running

- **Action**
  - Verify that the three-node Kafka cluster is up and running.
  - Open a new command window for executing Kafka commands.

### 2. Creating a New Kafka Topic with Three Partitions

- **Command Used**
  - `kafka-topics` tool for creating a topic.
- **Parameters**
  - **Topic Name:** Chosen topic name (e.g., `stock-ticks`).
  - **Number of Partitions:** Set to 3.
  - **Replication Factor:** Set appropriately (not specified, but typically 1 for a demo).
  - **Bootstrap Server:** Provide the address of one Kafka broker (e.g., `localhost:9092`).
- **Execution**
  - Run the command to create the topic with specified partitions.
- **Confirmation**
  - Verify that the topic is created successfully.

### 3. Starting Two Consumers in the Same Consumer Group

#### Consumer 1

- **Command Used**
  - `kafka-console-consumer`
- **Parameters**
  - **Bootstrap Server:** Address of one Kafka broker.
  - **Topic:** The topic created earlier.
  - **From Beginning:** Include `--from-beginning` to read from the start of the topic.
  - **Consumer Group:** Specify a group name (e.g., `group1`) using `--group group1`.
- **Execution**
  - Start the first consumer in a command window.

#### Consumer 2

- **Action**
  - Open a new command window.
- **Command Used**
  - Same as Consumer 1.
- **Execution**
  - Start the second consumer in the same group (`group1`).

#### Result

- **Observation**
  - Two consumers are now running in the same consumer group.
  - Both are connected to the Kafka cluster and are ready to consume messages from the topic.
- **Note**
  - At this point, no data is being consumed because no data has been produced yet.

### 4. Starting a Producer and Sending Data to Kafka

- **Data File**
  - A CSV file containing data (e.g., `datafile.csv`).
  - Contains 1,907 records.
- **Command Used**
  - `kafka-console-producer`
- **Parameters**
  - **Broker List:** Address of one Kafka broker (e.g., `localhost:9092`).
  - **Topic:** The topic to send data to.
- **Execution**
  - Use input redirection to send the contents of the data file to the producer:
    ```bash
    kafka-console-producer --broker-list localhost:9092 --topic stock-ticks < datafile.csv
    ```
- **Data Distribution**
  - Since the topic has three partitions, Kafka distributes the records across these partitions.
  - Records are assigned to partitions based on the partitioning strategy (default is round-robin or hash-based).

### 5. Observing Consumers and Data Consumption

- **Consumers in Action**
  - Both consumers start receiving data from the Kafka cluster.
  - The workload is shared between the consumers.
- **Data Processed**
  - **Consumer 1:** Processes 1,244 records.
  - **Consumer 2:** Processes 663 records.
- **Total Records Consumed**
  - Total records consumed by both consumers equal the total records sent (1,907).
- **Workload Sharing**
  - Kafka assigns partitions to consumers in a consumer group.
  - With three partitions and two consumers:
    - One consumer reads from two partitions.
    - The other consumer reads from one partition.

### 6. Investigating Data Storage in Kafka

- **Navigating to Kafka Log Directories**
  - Each Kafka broker has its own log directory where it stores data for partitions it manages.
  - Directories are named based on broker IDs (e.g., `kafka-logs-0`, `kafka-logs-1`, `kafka-logs-2`).
- **Examining Topic Partitions**
  - Inside each broker's log directory, there are directories for each topic and partition (e.g., `stock-ticks-0`, `stock-ticks-1`, `stock-ticks-2`).
- **Understanding Partition Distribution**
  - Partitions are distributed across the brokers in the cluster.
  - **Partition Numbers:**
    - Partitions are numbered starting from 0 (e.g., partition 0, partition 1, partition 2).
- **Using `kafka-dump-log` to Inspect Logs**
  - **Purpose:** To see the contents of the log files for each partition.
  - **Command:**
    ```bash
    kafka-dump-log --files /path/to/logfile --print-data-log
    ```
- **Analyzing Partition Data**
  - **Partition 0:**
    - Located on one of the brokers (e.g., broker 0).
    - Contains 653 records.
  - **Partition 1:**
    - Located on another broker (e.g., broker 1).
    - Contains 591 records.
  - **Partition 2:**
    - Located on the third broker (e.g., broker 2).
    - Contains 663 records.
- **Total Records in Partitions**
  - Sum of records across partitions:
    - 653 (Partition 0) + 591 (Partition 1) + 663 (Partition 2) = 1,907 records.
  - Matches the total number of records sent by the producer.

### 7. Mapping Consumers to Partitions

- **Consumer 1**
  - Likely assigned two partitions (e.g., partition 0 and partition 1).
  - Processes 1,244 records (653 + 591).
- **Consumer 2**
  - Assigned one partition (e.g., partition 2).
  - Processes 663 records.
- **Conclusion**
  - Workload is shared among consumers based on partition assignment.
  - Consumers in the same group divide the partitions among themselves.

## Key Learnings

### Kafka Cluster Data Storage

- **Partitions**
  - Topics are divided into partitions to allow for parallel processing and scalability.
  - Each partition is an ordered, immutable sequence of records.
- **Brokers**
  - Each broker in the cluster stores one or more partitions.
  - Brokers manage their assigned partitions and handle read/write requests.

### Consumer Groups and Workload Distribution

- **Consumer Groups**
  - A group of consumers that coordinate to consume data from a topic.
  - Consumers in the same group share the partitions of the topic.
- **Partition Assignment**
  - Kafka assigns partitions to consumers in a group to balance the load.
  - If there are more partitions than consumers, some consumers will handle multiple partitions.
- **Workload Sharing**
  - Enables horizontal scaling of data consumption.
  - Provides fault tolerance; if one consumer fails, Kafka reassigns its partitions to other consumers.

### Tools for Investigating Kafka Data

- **`kafka-dump-log`**
  - Used to inspect the contents of Kafka log files.
  - Can display detailed information about records, including offsets and data payloads.
- **Understanding Offsets**
  - **Offsets** are unique identifiers for records within a partition.
  - They help in tracking consumption progress and ensuring exactly-once processing.

### Practical Insights

- **Data Distribution**
  - Producers send data to Kafka, which distributes it across partitions based on the partitioning strategy.
- **Consumer Behavior**
  - Consumers read data from their assigned partitions independently.
  - The number of consumers should ideally not exceed the number of partitions for optimal resource utilization.
- **Cluster Operations**
  - Kafka's architecture allows for easy scaling by adding more brokers and partitions.
  - Data replication (not covered in detail here) provides fault tolerance and data durability.

## Conclusion

- **Summary**
  - Demonstrated how Kafka distributes data across partitions and brokers.
  - Showed how consumers in a group share the workload by consuming from assigned partitions.
  - Explored Kafka's storage mechanisms and tools for data inspection.
- **Key Takeaways**
  - Understanding Kafka's partitioning and consumer group mechanisms is crucial for building scalable and efficient data processing systems.
  - Kafka provides robust tools and features to manage data distribution and consumption.
- **Next Steps**
  - Experiment with different numbers of consumers and partitions to see how workload distribution changes.
  - Explore Kafka's replication features to understand fault tolerance.
  - Consider writing custom producer and consumer applications to implement business logic.
- **Encouragement**
  - Keep learning and experimenting with Kafka to deepen your understanding.
  - Utilize Kafka's rich ecosystem to build powerful streaming applications.

---

