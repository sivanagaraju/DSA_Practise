# Kafka Producer and Consumer Demo Mindmap

## Introduction

- **Objective**
  - Demonstrate Kafka producer and consumer in action using out-of-the-box tools.
  - Tools used:
    - **Kafka Console Producer**
    - **Kafka Console Consumer**
- **Setup**
  - **Data File**
    - A CSV file containing data to be sent to the Kafka cluster.
  - **Kafka Cluster**
    - Using a single-node Kafka cluster (could represent a larger cluster).

## Steps in the Demo

1. ### Create a Kafka Topic

   - **Tool Used**
     - `kafka-topics` command-line tool.
   - **Topic Name**
     - `test`
   - **Parameters to Specify**
     - **Number of Partitions**
       - **Considerations**
         - **Storage Requirement**
           - Small data set; fits into a single broker.
         - **Parallel Processing Requirement**
           - Single consumer; no need for parallel processing.
       - **Decision**
         - Use **a single partition**.
     - **Replication Factor**
       - **Definition**
         - Number of copies of each partition.
         - Provides fault tolerance.
       - **Considerations**
         - Multiple copies stored on different brokers.
         - In case of broker failure, data is still accessible.
       - **Decision**
         - Set replication factor to **1** (since we have a single broker).
     - **Cluster Coordinates**
       - **Parameter:** `--bootstrap-server`
       - **Value:** Kafka broker IP or hostname and listener port (default port **9092**).

2. ### Send Data to Kafka Using Console Producer

   - **Tool Used**
     - `kafka-console-producer`
   - **Target Topic**
     - `test`
   - **Cluster Coordinates**
     - **Parameter:** `--broker-list`
     - **Value:** Kafka broker IP/hostname and port (same as above).
     - **Note:** Different tools use different parameter names (`--bootstrap-server` vs `--broker-list`), but the value is the same.
   - **Input Data**
     - Kafka-console-producer can read input from a file.
     - Read the content of the CSV data file and send it to Kafka.

3. ### Consume Data from Kafka Using Console Consumer

   - **Tool Used**
     - `kafka-console-consumer`
   - **Source Topic**
     - `test`
   - **Cluster Coordinates**
     - **Parameter:** `--bootstrap-server`
     - **Value:** Kafka broker IP/hostname and port.
   - **Reading from the Beginning**
     - Use the parameter `--from-beginning` to read all data from the start of the topic.
   - **Output**
     - Display all records on the console.

## Demonstration Details

- **Data Transmission**
  - Sent data from the CSV file to Kafka topic `test`.
  - Consumer received all records and displayed them on the console.
- **Sending Additional Data**
  - If more data files are sent, the consumer immediately receives and displays the new data.

## Simulation Overview

- **Kafka Cluster**
  - **Single-Node Cluster**
    - Acts as the central broker in this demo.
    - In real scenarios, could be a multi-node cluster (e.g., 50-node cluster).
- **Data Source**
  - **Data Files**
    - Located on the same machine for the demo.
    - Could be on a remote machine or device connected over TCP/IP in real scenarios.
- **Producer Application**
  - Used an **off-the-shelf Kafka producer application** (`kafka-console-producer`).
  - **Considerations**
    - Could have written a custom producer.
    - `kafka-console-producer` suffices for sending data files.
- **Consumer Application**
  - Used `kafka-console-consumer` to read and process data.
  - **Processing**
    - Simple display of data on the console.
    - In real applications, the consumer could perform more complex processing.
  - **Location**
    - Consumer was on the same machine.
    - Could be remote, connecting over TCP/IP in other scenarios.

## Key Concepts and Learnings

- **Kafka Topics and Partitions**
  - Topics must be created before data can be sent.
  - **Number of Partitions**
    - Affects storage and parallel processing capabilities.
    - Single partition used due to small data size and single consumer.
- **Replication Factor**
  - Provides fault tolerance by storing copies on different brokers.
  - **Decision in Demo**
    - Set to 1 since only one broker is available.
- **Cluster Coordinates**
  - Necessary to connect to the Kafka cluster when using command-line tools.
  - **Parameters**
    - `--bootstrap-server` (for `kafka-topics` and `kafka-console-consumer`)
    - `--broker-list` (for `kafka-console-producer`)
  - **Values**
    - Kafka broker IP/hostname and port (default port 9092).
- **Using Console Tools**
  - `kafka-console-producer` and `kafka-console-consumer` are useful for simple data ingestion and consumption.
  - Handy for testing and demonstrations without writing custom code.
- **Data Flow in Kafka**
  - **Producers** send data to Kafka topics.
  - **Consumers** read data from Kafka topics.
  - Kafka acts as an intermediary, decoupling producers and consumers.

## Conclusion

- **Summary**
  - Successfully demonstrated sending and receiving data using Kafka.
  - Showed how to use Kafka command-line tools to interact with a Kafka cluster.
- **Highlights**
  - Importance of setting correct parameters when creating topics.
  - Understanding how replication factor and partitions affect data distribution and fault tolerance.
  - Recognition that simple tools can effectively facilitate data transmission and testing in Kafka.
- **Next Steps**
  - Explore writing custom producers and consumers for more complex processing.
  - Consider scenarios with multiple partitions and higher replication factors.
  - Experiment with remote producers and consumers over a network.

---
