# Kafka Topic and Partition Organization Mindmap

## Introduction

- **Context**
  - Previously learned that Apache Kafka organizes messages in topics.
  - Brokers create log files for each topic to store messages.
  - These log files are partitioned, replicated, and segmented.
- **Purpose of Lecture**
  - Explain and demonstrate Kafka log file organization.
  - Practical working session to show how topics and partitions are organized at the broker level.

## Kafka Topics

- **Definition**
  - A topic is a logical name to group messages.
  - Similar to a table in a database used to store data records.
  - In Kafka, you must create a topic to store messages.

- **Creating a Topic**
  - Requires specifying:
    - **Topic Name**
    - **Number of Partitions**
    - **Replication Factor**
  - If not specified, Kafka uses default values for partitions and replication factor.
  - **Command Structure**
    - On Linux: `kafka-topics.sh`
    - On Windows: `kafka-topics.bat`
    - Mandatory arguments:
      - `--create`: Indicates that you want to create a topic.
      - `--zookeeper`: Zookeeper coordinates (host and port).
      - `--topic`: Name of the topic.

## Kafka Cluster Setup

- **Three-Node Kafka Cluster**
  - Running locally on the machine.
  - Configured to work efficiently from IntelliJ IDEA.
  - All three brokers use the same `tmp` directory as their home directory.
    - **Benefit**: All data created by brokers resides in `tmp`, making it easy to monitor and understand internal processes.

- **Directory Structure**
  - **`tmp` Directory**
    - Contains data directories for:
      - **Zookeeper**
        - Stores Zookeeper's data.
        - Zookeeper is essential for Kafka's operation (detailed explanation in a different lecture).
      - **Kafka Brokers**
        - Each broker has its own data directory within `tmp`.
    - **Initial State**
      - Before any topics are created, brokers have initial files in their data directories.
      - These files are mostly empty.
      - No topic-specific files exist yet.

## Understanding Topic Partitions

- **Need for Partitions**
  - A single topic may store millions of messages.
  - Storing all messages in a single file is impractical due to size and performance considerations.

- **What is a Partition?**
  - A mechanism to break a topic into smaller, more manageable parts.
  - **In Kafka:**
    - A partition is a physical directory on the broker's filesystem.
    - Each partition corresponds to a separate directory.
  - **Purpose of Partitions**
    - Facilitates scalability and parallel processing.
    - Allows Kafka to distribute data across multiple brokers.

- **Creating Partitions**
  - When creating a topic, you specify the number of partitions using `--partitions`.
  - Kafka creates one directory per partition.
  - **Example:**
    - Creating a topic named `invoices` with 5 partitions results in 5 directories:
      - `invoices-0`
      - `invoices-1`
      - `invoices-2`
      - `invoices-3`
      - `invoices-4`
  - **Directory Naming Convention**
    - The directory name includes the topic name and partition number.
    - Partition numbers start from 0.

## Demonstration Steps

1. **Starting the Kafka Cluster**
   - Ensure the three-node Kafka cluster is up and running.
   - Brokers are configured to use the `tmp` directory for data storage.

2. **Inspecting the `tmp` Directory Before Topic Creation**
   - Contains:
     - `zookeeper` directory: Holds Zookeeper data.
     - Directories for each Kafka broker (e.g., `kafka-logs-0`, `kafka-logs-1`, `kafka-logs-2`).
   - Initial files in broker directories are present but mostly empty.
   - No topic-specific directories yet.

3. **Creating a Topic**
   - **Command Used:**
     ```bash
     kafka-topics --create --zookeeper localhost:2181 --topic invoices --partitions 5 --replication-factor 1
     ```
     - `--create`: Create a new topic.
     - `--zookeeper`: Specify Zookeeper coordinates (e.g., `localhost:2181`).
     - `--topic`: Name of the topic (`invoices`).
     - `--partitions`: Number of partitions (e.g., `5`).
     - `--replication-factor`: Number of replicas (e.g., `1` for simplicity).

   - **Execution:**
     - Run the command in the terminal.
     - Kafka acknowledges the creation of the topic.

4. **Inspecting the `tmp` Directory After Topic Creation**
   - New directories appear in the broker data directories corresponding to the topic partitions.
   - **Example:**
     - Inside a broker's data directory, you might see:
       - `invoices-0`
       - `invoices-1`
       - `invoices-2`
       - `invoices-3`
       - `invoices-4`
   - Each directory represents a partition of the `invoices` topic.

5. **Understanding the Results**
   - **Kafka Topic Partitions as Directories:**
     - For each partition specified during topic creation, Kafka creates a separate directory.
     - This physical separation helps in data management and retrieval.
   - **Scalability:**
     - Partitions enable Kafka to handle large volumes of data efficiently.
     - They allow for parallel processing and load distribution across brokers.

## Key Takeaways

- **Kafka Topic Partitions:**
  - Essential for managing large datasets.
  - Provide a way to divide data for better performance and scalability.
  - Physically represented as directories on the filesystem.

- **Topic Creation Parameters:**
  - **Number of Partitions (`--partitions`):**
    - Determines how the data is split.
    - More partitions can improve parallelism but may add complexity.
  - **Replication Factor (`--replication-factor`):**
    - Specifies how many copies of the data are stored across brokers.
    - Higher replication increases fault tolerance.

- **Broker Data Organization:**
  - Each broker manages its own set of partitions.
  - Data is organized neatly within directories for each topic and partition.

- **Practical Insights:**
  - Monitoring the broker directories can provide valuable insights into how Kafka stores and manages data.
  - Understanding the physical layout helps in troubleshooting and optimizing Kafka clusters.

## Conclusion

- **Summary:**
  - Demonstrated how Kafka topics and partitions are organized at the broker level.
  - Showed that partitions are implemented as directories, making data storage efficient.
  - Highlighted the importance of specifying partitions and replication factor during topic creation.

- **Next Steps:**
  - Further exploration of Kafka internals, such as message replication and segmenting.
  - Understanding how Zookeeper coordinates with Kafka brokers.

- **Closing Remarks:**
  - Encouraged continuous learning and exploration of Kafka.
  - Emphasized the value of understanding underlying concepts for effective use of Kafka.

---

**Note:** This mindmap captures all the information from the lecture, organized hierarchically to provide a clear understanding of Kafka topic and partition organization. Each section is detailed to ensure no information is missed.