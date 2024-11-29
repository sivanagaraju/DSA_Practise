# Minimum In-Sync Replicas in Kafka Mindmap

## Introduction

- **Recap of Previous Lecture**
  - Learned about **committed and uncommitted messages**
  - Discussed their relation to the **ISR (In-Sync Replicas) list**

- **Purpose of This Lecture**
  - Extend the idea further
  - Learn about the **Minimum In-Sync Replicas** configuration in Kafka

---

## Data Commitment in Kafka

- **Definition of Committed Data**
  - Data is considered **committed when written to all In-Sync Replicas (ISR)**
  
- **Initial Scenario**
  - Start with **3 replicas**
  - All replicas are healthy and part of the **ISR**

---

## Failure of Replicas and Impact on ISR

- **Replica Failures**
  - After some time, **two replicas fail**
  - Leader removes the failed replicas from the **ISR**

- **Resulting State**
  - Left with a **single In-Sync Replica** (the leader itself)

- **Data Commitment in This State**
  - Data is still considered committed when written to all ISR
  - Now, **"all" means just the leader**

---

## Risk to Data Consistency

- **Risky Scenario**
  - If the **leader fails**, data could be **lost**
  - Data exists only on one replica (no redundancy)

- **Need for Protection**
  - Kafka provides a mechanism to prevent data loss in such scenarios
  - Introduces the concept of **Minimum In-Sync Replicas**

---

## Minimum In-Sync Replicas Configuration

- **Purpose of Minimum ISR**
  - Ensures that data is replicated to a **minimum number of replicas** before being considered committed

- **Setting Minimum ISR**
  - Configure the topic with **`min.insync.replicas`**
  - Example: Set **`min.insync.replicas=2`** to require data to be on at least **2 replicas**

- **Effect on Data Commitment**
  - Data is only considered committed when written to **at least 2 ISR replicas**
  - Enhances data durability and consistency

---

## Side Effects of Setting Minimum ISR

- **Write Availability Impact**
  - With **3 replicas** and **`min.insync.replicas=2`**
  - You can **only write** to a partition if **at least 2 out of 3 replicas are in-sync**

- **When Replicas Are Not In-Sync**
  - If fewer than **2 replicas** are in the ISR:
    - Broker will **not accept new messages**
    - Broker responds with **"Not Enough Replicas" exception**

- **Leader Becomes Read-Only**
  - You can **read** from the partition
  - You **cannot write** until another replica rejoins the ISR

- **Recovery Steps**
  - Bring the failed replicas **back online**
  - Allow replicas to **catch up** and become **in-sync**
  - Once **minimum ISR** is satisfied, writes can resume

- **Trade-Off**
  - **Data Consistency** over **Write Availability**
  - Ensures data is not lost but may temporarily prevent writes

---

## Conclusion

- **Summary**
  - Setting **Minimum In-Sync Replicas** helps prevent data loss
  - Important for scenarios where **data consistency** is critical

- **Acknowledgement of Complexity**
  - Concepts may seem **overwhelming**

- **Reassurance**
  - These topics will be revisited with **practical examples**
  - Understanding will improve with **hands-on experience**

- **Closing Remarks**
  - "That's all I wanted to cover in this session."
  - "See you in the next lecture."
  - "**Keep learning and keep growing.**"

---