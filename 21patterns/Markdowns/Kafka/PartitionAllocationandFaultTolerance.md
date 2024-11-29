# Kafka Work Distribution and Fault Tolerance Mindmap

## Introduction

- **Context**
  - Previous sessions explored:
    - **Kafka Log Files**
    - **Cluster Formation**
  - Next step:
    - Understanding the **relationship between log files and cluster formation**
    - How work is distributed among brokers in a Kafka cluster
    - What makes Kafka a **scalable** and **fault-tolerant** system

## Kafka Topic Organization

- **Topics Broken into Independent Partitions**
  - **Partitions are Self-Contained**
    - All partition information (segment files, indexes) stored in the same directory
  - **Benefits**
    - Efficient distribution of work among brokers
    - Easy to assign partitions to different brokers

- **Responsibility Distribution**
  - When a topic is created:
    - **Creation, storage, and management of partitions are distributed among brokers**
    - Each broker is responsible for one or more assigned partitions
  - **Result**
    - Work is shared among brokers
    - Facilitates scalability and load balancing

## Example Scenario: Partition Allocation in a Kafka Cluster

### Cluster Setup

- **Kafka Cluster**
  - Consists of **6 brokers**
  - Brokers are running on individual machines
- **Rack Organization**
  - Machines are organized into **2 racks**
    - **Rack 1:** Brokers 0, 1, 2
    - **Rack 2:** Brokers 3, 4, 5

### Topic Creation Parameters

- **Topic with:**
  - **10 Partitions**
  - **Replication Factor of 3**
- **Total Replicas to Allocate**
  - **10 partitions × 3 replicas = 30 replicas**

### Goals for Partition Allocation

1. **Even Distribution of Partitions**
   - Achieve workload balance among brokers
   - Distribute partitions as evenly as possible

2. **Fault Tolerance**
   - Place follower partitions (duplicate copies) on different machines
   - Ensure that if a broker or rack fails, partitions are still accessible
   - Achieve high availability

### Steps for Partition Allocation

#### 1. Create an Ordered List of Brokers

- **Process**
  - Start with a randomly chosen broker in a rack
  - Alternate brokers from different racks
- **Ordered Broker List**
  1. **Broker 0** (Rack 1)
  2. **Broker 3** (Rack 2)
  3. **Broker 1** (Rack 1)
  4. **Broker 4** (Rack 2)
  5. **Broker 2** (Rack 1)
  6. **Broker 5** (Rack 2)

#### 2. Assign Partitions to Brokers

- **Objective**
  - Use the ordered list to assign leaders and followers in a round-robin fashion

##### Assigning Leader Partitions

- **Method**
  - Start from the first broker in the list
  - Assign leaders for each partition sequentially
- **Assignments**
  - **Partition 0 Leader → Broker 0**
  - **Partition 1 Leader → Broker 3**
  - **Partition 2 Leader → Broker 1**
  - **Partition 3 Leader → Broker 4**
  - **Partition 4 Leader → Broker 2**
  - **Partition 5 Leader → Broker 5**
  - **Partition 6 Leader → Broker 0**
  - **Partition 7 Leader → Broker 3**
  - **Partition 8 Leader → Broker 1**
  - **Partition 9 Leader → Broker 4**

##### Assigning First Followers

- **Method**
  - Start from the **second broker** in the list
  - Skip the first broker
  - Use round-robin assignment
- **Assignments**
  - **Partition 0 First Follower → Broker 3**
  - **Partition 1 First Follower → Broker 1**
  - **Partition 2 First Follower → Broker 4**
  - **Partition 3 First Follower → Broker 2**
  - **Partition 4 First Follower → Broker 5**
  - **Partition 5 First Follower → Broker 0**
  - **Partition 6 First Follower → Broker 3**
  - **Partition 7 First Follower → Broker 1**
  - **Partition 8 First Follower → Broker 4**
  - **Partition 9 First Follower → Broker 2**

##### Assigning Second Followers

- **Method**
  - Start from the **third broker** in the list
  - Skip the first two brokers
  - Use round-robin assignment
- **Assignments**
  - **Partition 0 Second Follower → Broker 1**
  - **Partition 1 Second Follower → Broker 4**
  - **Partition 2 Second Follower → Broker 2**
  - **Partition 3 Second Follower → Broker 5**
  - **Partition 4 Second Follower → Broker 0**
  - **Partition 5 Second Follower → Broker 3**
  - **Partition 6 Second Follower → Broker 1**
  - **Partition 7 Second Follower → Broker 4**
  - **Partition 8 Second Follower → Broker 2**
  - **Partition 9 Second Follower → Broker 5**

### Outcome Analysis

- **Distribution of Partitions**
  - Not perfectly even due to fault tolerance constraints
  - **Broker Partition Counts:**
    - **Broker 0:** 4 partitions
    - **Broker 1:** 5 partitions
    - **Broker 2:** 5 partitions
    - **Broker 3:** 5 partitions
    - **Broker 4:** 6 partitions
    - **Broker 5:** 5 partitions
- **Workload Balance**
  - Slight disparity in partition counts
  - Acceptable for achieving fault tolerance

### Fault Tolerance Evaluation

- **Cross-Rack Replication**
  - Leaders and followers placed on different racks
- **Example: Partition 4**
  - **Leader:** Broker 2 (Rack 1)
  - **First Follower:** Broker 5 (Rack 2)
  - **Second Follower:** Broker 0 (Rack 1)
- **Resilience to Failures**
  - If one broker fails, other brokers have replicas
  - If an entire rack fails, replicas on other rack ensure availability
- **Overall**
  - At least two copies of each partition are on different racks
  - High availability and fault tolerance are achieved

## Key Takeaways

- **Work Distribution**
  - Brokers share responsibility by managing assigned partitions
- **Scalability**
  - Partitions can be added, and brokers can manage multiple partitions
- **Fault Tolerance**
  - Replication across brokers and racks ensures data availability
  - Kafka's partition assignment aims to minimize data loss risk
- **Partition Assignment Strategy**
  - Uses an ordered broker list and round-robin allocation
  - Alternates brokers across racks for replication

## Conclusion

- **First Half of Work Distribution**
  - Understanding how replicas are distributed among brokers
- **Second Half**
  - Defining the responsibilities of individual brokers (to be discussed in the next lecture)
- **Final Remarks**
  - Kafka's design allows for efficient scaling and fault tolerance
  - The partitioning and replication strategy is key to Kafka's robustness
- **Next Steps**
  - Further exploration of broker responsibilities in managing partitions

---
