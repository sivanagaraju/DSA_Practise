# Advanced Kafka Producers: Creating a Multi-Threaded Kafka Producer Mindmap

## Introduction

- **Objective**
  - Create a scenario to understand and implement a multi-threaded Kafka producer.
- **Problem Statement**
  - Assume you have multiple data files and want to send data from all those files to a Kafka cluster.
  - **Goal**: Create a main thread that reads multiple data files and creates an independent thread for each file to process and send data to Kafka.

## Solution Overview

- **Approach**
  - Use one main thread to manage data files and threads.
  - For each data file, create a separate thread to process and send data.
  - **Best Practice**: Share the same Kafka producer instance among all threads to optimize resource usage.

## Starter Project Setup

- **Included Components**
  - **Maven `pom.xml`**: Defines project dependencies.
  - **Pre-configured `log4j2.xml`**: For logging.
  - **Scripts**:
    - Start Kafka cluster.
    - Create Kafka topics.
    - Start a console consumer to view received messages.
  - **Sample Data Files**: Two data files to test the producer.
  - **`AppConfigs` Class**: Contains constants used in the code.
  - **`Kafka.properties` File**:
    - Holds producer-level configurations.
    - Keeps Kafka broker coordinates outside the application code.
    - Allows for easy connection changes without modifying source code.

## Implementation Details

### Required Classes

1. **`Dispatcher` Class**
   - **Purpose**: Implements `Runnable` to create a thread for each data file.
   - **Responsibilities**:
     - Read all records from a given data file.
     - Send all records to a specified Kafka topic using a shared producer instance.
   - **Members**:
     - `private String topicName;`
     - `private String filePath;`
     - `private Producer<Integer, String> producer;`
   - **Constructor**:
     - Accepts `producer`, `topicName`, and `filePath` as parameters.
   - **Methods**:
     - **`run()`**:
       - Overrides `Runnable`'s `run` method.
       - Steps:
         1. Get a handle to the data file.
         2. Create a `Scanner` to read the file.
         3. Loop through each line in the file:
            - Send each line to Kafka using `producer.send()`.
         4. Optionally, add logging and line counting.

2. **`DispatcherDemo` Class**
   - **Purpose**: Contains the `main` method to initiate the application.
   - **Responsibilities**:
     - Create and configure the Kafka producer.
     - Create threads for each data file and start them.
     - Wait for all threads to complete.
     - Close the producer after completion.
   - **Methods**:
     - **`main(String[] args)`**:
       - Steps:
         1. Create a `Properties` object for producer configurations.
            - Load properties from `Kafka.properties` file.
            - Add any additional necessary configurations.
         2. Instantiate a shared `KafkaProducer`.
         3. Prepare an array to hold thread references.
         4. Loop through the data files:
            - Create a `Dispatcher` thread for each file.
            - Pass the shared producer, topic name, and file path.
            - Start each thread.
         5. Wait for all threads to finish using `Thread.join()`.
         6. Close the Kafka producer.

### Implementation Steps

1. **Creating the `Dispatcher` Class**
   - Implement `Runnable` to allow threading.
   - Define private members for `topicName`, `filePath`, and `producer`.
   - Create a constructor to initialize these members.
   - Override the `run()` method:
     - Use a `Scanner` to read the file line by line.
     - Send each line to Kafka using the producer.
     - Handle exceptions with try-catch blocks.
     - Optionally, add logging messages for start and finish.

2. **Creating the `DispatcherDemo` Class**
   - Define the `main` method.
   - Load properties from `Kafka.properties` using `FileInputStream`.
   - Add additional producer configurations directly to the `Properties` object.
   - Create a `KafkaProducer<Integer, String>` instance using the properties.
   - Prepare an array to hold `Thread` objects for each data file.
   - Loop through the data files:
     - Instantiate a `Dispatcher` for each file.
     - Create a new `Thread` with the `Dispatcher` instance.
     - Start the thread.
   - Use a second loop to `join()` all threads, ensuring the main thread waits for completion.
   - Close the producer after all threads have finished.

### Key Points

- **Shared Producer Instance**
  - All threads share the same `KafkaProducer` instance to optimize resource usage.
  - Avoids creating multiple producer instances within the same application.
- **Thread Management**
  - Using `Runnable` and `Thread` classes to manage concurrency.
  - `Thread.join()` ensures the main thread waits for worker threads to finish.
- **Exception Handling**
  - Proper try-catch blocks are used to handle potential IO exceptions.
- **Logging**
  - Optional logging messages can be added to monitor the progress of each thread.

## Execution Steps

1. **Start Zookeeper**
   - Use the provided script to start Zookeeper, which is required for Kafka.

2. **Start Kafka Brokers**
   - Start all Kafka broker instances using the provided scripts.

3. **Create Kafka Topic**
   - Use the provided script to create the necessary Kafka topic.

4. **Run the Producer Application**
   - Execute the `DispatcherDemo` class.
   - The application reads data files and sends messages to Kafka.

5. **Verify Message Delivery**
   - Use a Kafka console consumer to view the messages received by the topic.

6. **Re-Execution**
   - Running the producer application again will resend all data from the files.

7. **Clean Start (Optional)**
   - To start fresh:
     - Stop Kafka brokers and Zookeeper.
     - Delete the `tmp` directory (contains data for Zookeeper and Kafka brokers).
     - Restart Zookeeper and Kafka brokers.
     - Kafka server will start without previous data.

## Summary

- **Implementation Recap**
  - Created a `Dispatcher` class to handle file processing in separate threads.
  - Created a `DispatcherDemo` class to manage threads and the Kafka producer.
  - Shared a single `KafkaProducer` instance across all threads.
  - Used multi-threading to process and send data files to Kafka in parallel.
- **Benefits**
  - Efficient resource utilization by sharing the producer.
  - Increased throughput by parallel processing of data files.
  - Scalability for applications needing to handle large volumes of data.

## Conclusion

- **Outcome**
  - Successfully implemented a multi-threaded Kafka producer application.
- **Best Practices Highlighted**
  - Sharing resources (like the Kafka producer) across threads when thread-safe.
  - Externalizing configurations to properties files for flexibility.
  - Proper thread management using `Runnable` and `Thread.join()`.
- **Next Steps**
  - Experiment with more data files or larger datasets.
  - Enhance error handling and logging.
  - Explore more complex data processing before sending to Kafka.
- **Final Remarks**
  - Understanding multi-threaded producers is essential for high-throughput applications.

---

