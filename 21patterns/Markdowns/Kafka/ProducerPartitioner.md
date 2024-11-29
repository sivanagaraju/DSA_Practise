# Kafka Producer Partitioner Mindmap

## Introduction

- **Recap**
  - Previously learned about producer serialization.
- **Next Topic**
  - Understanding the **Partitioner** in Kafka Producer.

## Producer Record and Topic Partitioning

- **Producer Record Components**
  - Includes a **mandatory topic name** as the destination address of the data.
- **Kafka Topics are Partitioned**
  - Producers must decide **which partition** to send each message to.

## Approaches to Specify Target Partition

1. **Set Partition Number in Producer Record**
   - **Method**
     - Supply the partition number as an argument in the `ProducerRecord`.
   - **Usage**
     - **Rarely used** approach.

2. **Supply a Partitioner Class**
   - **Method**
     - Implement a partitioner class that determines the partition number at runtime.
     - Assigns a partition number to each message.
   - **Specification**
     - Specify a custom partitioner using the **properties object**.
   - **Usage**
     - **Commonly used** approach.

## Default Partitioner

- **Availability**
  - Kafka Producer comes with a **default partitioner**.
- **Usage**
  - Most commonly used in practice.
- **Partitioning Strategies Used**

### 1. Hash Key Partitioning

- **Applicable When**
  - **Message key exists**.
- **Process**
  - Uses a **hashing algorithm** on the key to determine the partition number.
  - Steps:
    - Hash the key to get a numeric value.
    - Calculate `partition number = hash(key) % number of partitions`.
- **Benefits**
  - Ensures all messages with the **same key** go to the **same partition**.
- **Considerations**
  - The algorithm depends on the **total number of partitions**.
  - **Implications of Changing Partitions**
    - Increasing the number of partitions can change the partitioning outcome.
    - Messages with the same key may go to different partitions after the change.
- **Recommendations**
  - **Create Topic with Sufficient Partitions Initially**
    - Avoid increasing partitions later.
  - **Overprovision Partitions**
    - For example, if you need 100 partitions, create 125 partitions.
    - Little harm in overprovisioning.
  - **Redistribution**
    - If partitions are increased later, existing messages may need to be redistributed.

### 2. Round Robin Partitioning

- **Applicable When**
  - **Message key is null**.
- **Process**
  - Uses a **round-robin method** to distribute messages equally.
  - Steps:
    - First message goes to Partition 0.
    - Next message goes to Partition 1.
    - Continues cycling through partitions.
- **Benefits**
  - Achieves **equal distribution** among available partitions.

## Custom Partitioner

- **Flexibility**
  - Kafka allows implementing custom partitioning strategies.
- **Implementation**
  - Create a custom partitioner class.
  - Specify it using the **properties object**.
- **Usage**
  - **Often Not Necessary**
    - The default partitioner meets most use cases.

## Conclusion

- **Default Partitioner Suffices for Most Cases**
  - Handles both key-based and key-less messages efficiently.
- **Understanding Partitioning is Crucial**
  - Impacts data distribution and message ordering.
- **Final Remarks**
  - Great. See you again.
  - **Keep learning and keep growing.**

---