# Kafka Producer Example Mindmap

## Introduction

- **Objective**: Understand the mechanics of sending events to Apache Kafka through practical examples.
- **Approach**: Problem-solution method.

## Problem Statement

- **Goal**: Create the simplest possible Kafka producer code that sends **one million string messages** to a Kafka topic.

## Project Setup

- **Project Name**: `hello-producer`
- **Project Type**: Maven project
- **Integrated Development Environment (IDE)**: IntelliJ IDEA
- **Starter Project**:
  - Included in course materials.
  - Download and open in IntelliJ IDEA.
- **Project Setup Includes**:
  - **`pom.xml`**:
    - Contains all required dependencies.
  - **`log4j2.xml`**:
    - Configuration file for logging.
  - **`AppConfig` Class**:
    - Contains static constants for configurations.
    - Constants will be used in the example.
  - **Scripts**:
    - To start the Kafka cluster on the local machine.
    - Using a **three-node Kafka cluster** setup.

## Creating the Producer

### Step 1: Create a Class with Main Method

- **Class Name**: `HelloProducer`
- **Define a Logger**:
  - Not mandatory but good practice.
  - Helps create log entries.
- **Create the `main` Method**:
  - Entry point of the application.
- **Log Entry**:
  - Place a log entry to indicate the program has started.

### Step 2: Sending Data to Kafka - Multi-Step Process

#### 1. Create Java Properties Object and Set Configurations

- **Kafka Producer API**:
  - Highly configurable.
  - Behavior customized via producer configurations.
- **Four Basic Configurations** (Bare minimum for the producer to work):

  a. **`CLIENT_ID_CONFIG`**:
     - A simple string passed to the Kafka server.
     - **Purpose**: To track the source of the message.

  b. **`BOOTSTRAP_SERVERS_CONFIG`**:
     - Comma-separated list of `host:port` pairs.
     - **Purpose**: Used by the producer to establish the initial connection to the Kafka cluster.
     - **Notes**:
       - For single-node Kafka, supply individual `host:port` information.
       - Used **only** for the initial connection.
       - Once connected, the producer queries for metadata to discover the full list of Kafka brokers.
       - Recommended to provide 2-3 broker addresses in a multi-node cluster to handle cases where the first broker is down.

  c. **Key Serializer**:
     - Specifies the serializer class for the message key.
     - **In this example**: `IntegerSerializer`.

  d. **Value Serializer**:
     - Specifies the serializer class for the message value.
     - **In this example**: `StringSerializer`.

- **Constants in `AppConfig`**:
  - Configuration values are defined as constants.
  - Promotes reusability and cleaner code.

- **Concepts**:

  1. **Key-Value Pair**:
     - Each Kafka message has a key and a value.
     - The key can be `null`, but the message is still structured as a key-value pair.
     - **Importance**:
       - Keys are used for message partitioning and can impact message ordering.

  2. **Serializer**:
     - Messages are sent over the network; key and value must be serialized into bytes.
     - Kafka provides ready-to-use serializer classes.
     - **In this example**:
       - **Key Serializer**: `IntegerSerializer`.
       - **Value Serializer**: `StringSerializer`.

#### 2. Create an Instance of `KafkaProducer`

- **Key Type**: `Integer`
- **Value Type**: `String`
- **Constructor Parameters**:
  - The properties object created earlier.
- **Purpose**:
  - Establishes a connection to the Kafka cluster.
  - Manages the sending of messages.

#### 3. Start Sending Messages to Kafka

- **Create a Loop**:
  - Executes **one million times**.
  - **Purpose**: To send a high volume of messages.
- **Inside the Loop**:
  - **Send Messages Using the `send` Method**:
    - The `send` method takes a `ProducerRecord` object.
    - Sends it asynchronously to the Kafka cluster.
  - **Create a `ProducerRecord`**:
    - **Constructor Arguments**:
      1. **Topic Name**:
         - The name of the Kafka topic to send messages to.
      2. **Message Key**:
         - In this example, the loop counter (an integer).
         - **Purpose**: Can influence partitioning and ordering.
      3. **Message Value**:
         - A simple string message.
         - To keep it unique, concatenate the loop counter.
         - Example: `"Simple Message-" + i`

- **Note on Message Sending**:
  - Messages are sent asynchronously.
  - The `send` method returns immediately and uses a background thread.

#### 4. Close the Producer Instance

- **After the Loop Completes**:
  - One million string messages have been sent to the Kafka cluster.
- **Importance of Closing the Producer**:
  - The producer has buffer space and a background I/O thread.
  - Not closing the producer can lead to resource leaks and incomplete message sending.
  - **Best Practice**: Always close the producer after sending all required messages.

### Summary of Steps

1. **Set Configurations**:
   - Control the behavior of the producer.
   - Essential configurations include client ID, bootstrap servers, and serializers.

2. **Create Producer Object**:
   - An instance of `KafkaProducer`.
   - Handles the connection and message sending.

3. **Send Messages**:
   - Use a loop to send messages.
   - Messages are sent asynchronously using the `send` method.

4. **Close Producer**:
   - Release resources by closing the producer instance.
   - Ensures all buffered messages are sent and resources are cleaned up.

## Execution

- **Scripts Included**:
  - Scripts to start Zookeeper and Kafka brokers are included in the starter project.
- **Execution Steps**:

  1. **Start Zookeeper**:
     - Necessary for Kafka to run.
     - **Command**: Run the provided script (e.g., `start-zookeeper.sh`).

  2. **Start All Three Kafka Brokers**:
     - Ensures high availability and replication.
     - **Command**: Run the provided scripts for each broker (e.g., `start-kafka-1.sh`, `start-kafka-2.sh`, `start-kafka-3.sh`).
     - **Note**: Wait for the brokers to fully start before proceeding.

  3. **Create the Topic**:
     - The topic to which messages will be sent.
     - **Command**: Use the provided script (e.g., `create-topic.sh`).
     - **Topic Configuration**:
       - You can specify the number of partitions and replication factor.

  4. **Execute the Example**:
     - Run the `HelloProducer` class from the IDE or command line.
     - **Observation**: Monitor logs to ensure the producer is running.

  5. **Sending Messages**:
     - Start sending messages.
     - The process finishes sending messages.
     - **Performance**:
       - It takes a few seconds to send one million small messages.
       - Actual time may vary based on system performance.

- **Validation**:
  - Verify that messages are received in Kafka.
  - Use Kafka tools or consumer applications to confirm.

## Conclusion

- **Next Steps**:
  - In the next video, we will learn some internals of the Kafka producer.
  - Topics may include batching, partitions, acknowledgments, and error handling.

- **Encouragement**:
  - Practice by creating and modifying the example.
  - Experiment with different configurations and observe the effects.
  - **Keep learning and keep growing.**

---
