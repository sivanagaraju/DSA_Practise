# Kafka Replication Factor Mindmap

## Introduction

- **Context**
  - Continuation from the previous lecture on Kafka topics and partitions.
  - Focus on understanding the **Replication Factor** in Apache Kafka.

## What is the Replication Factor?

- **Definition**
  - The **Replication Factor** specifies **how many copies of each partition** you want to maintain across the Kafka cluster.
  - It is a critical parameter for **fault tolerance** and **data redundancy**.
- **Purpose**
  - Ensures that data remains available even if some brokers fail.
  - Each copy of a partition is called a **replica**.

## Relationship Between Replication Factor and Partitions

- **Multiplicative Effect**
  - The Replication Factor multiplies with the number of partitions to determine the **total number of partition replicas**.
  - **Formula:**
    ```
    Total Partition Replicas = Number of Partitions × Replication Factor
    ```
- **Implication**
  - Higher Replication Factor increases fault tolerance but requires more storage across brokers.
  - The total number of directories created corresponds to the total partition replicas.

## Example Scenario

- **Topic Creation**
  - **Topic Name:** `invoices`
  - **Number of Partitions:** 5
  - **Replication Factor:** 3
- **Expected Outcome**
  - Kafka should create:
    ```
    5 partitions × 3 replicas = 15 directories (partition replicas)
    ```
- **Observation**
  - Initially, only 5 directories were observed on one broker.
  - **Question Raised:** Where are the other 10 directories?

## Location and Distribution of Partition Replicas

- **Distribution Across Brokers**
  - The additional directories (partition replicas) are created on the **other brokers** in the cluster.
- **Explanation**
  - In a Kafka cluster, partitions and their replicas are distributed among all available brokers.
  - Each broker stores a subset of the total partition replicas.
- **Verification**
  - Checking the data directories (home directories) of the other two brokers reveals they also have 5 directories each for the `invoices` topic.
- **Total Count**
  - **On Each Broker:** 5 directories (one for each partition replica assigned to that broker).
  - **Across All Brokers:** 5 partitions × 3 replicas = **15 directories**.
- **Terminology**
  - These directories are known as **partition replicas**.

## Naming and Organization of Partition Replicas

- **Naming Convention**
  - For **Partition 0**:
    - **1st Replica** of Partition 0 (e.g., on Broker 1)
    - **2nd Replica** of Partition 0 (e.g., on Broker 2)
    - **3rd Replica** of Partition 0 (e.g., on Broker 3)
  - The same pattern applies to **Partitions 1** through **4**.
- **Understanding Replicas**
  - Each partition has **multiple replicas**, one on each broker, as determined by the Replication Factor.
  - Replicas ensure that each partition's data is duplicated across the cluster for reliability.

## Summary and Key Takeaways

- **Replication Factor Impact**
  - The number of partitions and the Replication Factor multiply to result in the total number of partition replicas.
  - This affects how data is stored and replicated across the cluster.
- **Formula Recap**
  - ```
    Total Partition Replicas = Number of Partitions × Replication Factor
    ```
- **Example Recap**
  - With **5 partitions** and a **Replication Factor of 3**:
    - **Total Partition Replicas:** 5 × 3 = **15**
    - **Total Directories Created:** 15 (distributed among brokers)
- **Distribution**
  - Partition replicas are spread across available brokers to ensure fault tolerance.
  - All replicas are part of the same topic but reside on different brokers.

## Conclusion

- **Key Point**
  - Understanding the Replication Factor is crucial for configuring Kafka for high availability and fault tolerance.
- **Final Thoughts**
  - The distribution of partition replicas across brokers helps Kafka provide data redundancy and resilience against broker failures.
- **Encouragement**
  - Continue exploring Kafka's architecture to deepen your understanding.
- **Closing Remarks**
  - See you again in the next lecture.
  - **Keep learning and keep growing.**

---

**Note:** This mindmap captures all the information from the lecture on Kafka's Replication Factor, including definitions, examples, calculations, and explanations of how partition replicas are distributed across brokers. It ensures that no details are missed and provides a comprehensive understanding of the topic.