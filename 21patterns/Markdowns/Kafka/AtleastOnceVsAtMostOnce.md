# At Least Once vs. At Most Once Semantics in Apache Kafka Mindmap

## Introduction

- **Recap of Previous Lectures**
  - Learned to create Kafka producers.
  - Assumption: Comfortable with basic requirements of streaming events to the Kafka cluster.
- **Advanced Producer Concepts**
  - Some specific and intricate scenarios require extra attention.
  - Topic: **At Least Once vs. At Most Once Semantics**.

---

## Kafka's Message Durability Guarantee

- **Message Commitment**
  - Apache Kafka provides message durability by committing messages to the **partition log**.
- **Definition of Durability**
  - Once data is **persisted by the leader broker** in the leader partition, the message cannot be lost **as long as the leader is alive**.
- **Limitation**
  - If the **leader broker goes down**, there is a risk of data loss.

---

## Replication in Kafka

- **Purpose of Replication**
  - To **protect against data loss** due to leader failure.
- **Implementation**
  - Kafka uses **followers** to replicate data.
- **Followers' Role**
  - **Copy messages** from the leader.
  - Provide **fault tolerance** in case of leader failure.
- **Full Commitment of Messages**
  - When data is persisted to both the **leader** and the **followers in the ISR (In-Sync Replicas) list**.
  - Message is considered **fully committed**.
- **High Durability**
  - Once fully committed, data cannot be lost unless **both the leader and all replicas fail** (unlikely scenario).

---

## Possibility of Duplicate Messages

- **Producer Retry Mechanism**
  - Even with replication, there's a possibility of **committing duplicate messages**.
- **Why Duplicates Occur**
  - If the producer's I/O thread fails to receive a success **acknowledgement** from the broker, it **retries sending the message**.

### Scenario Leading to Duplicate Messages

1. **Message Transmission**
   - The **I/O thread** sends a record to the broker.
2. **Broker Receives Message**
   - Broker **receives the data** and stores it in the partition log.
3. **Broker Sends Acknowledgement**
   - Broker sends a **success acknowledgement**.
4. **Network Error**
   - The **acknowledgement does not reach** back to the I/O thread due to a **network error**.
5. **Producer Retries**
   - I/O thread **waits** and then **resends the record**, assuming failure.
6. **Duplicate Message Reception**
   - Broker receives the **same data again**.
   - Broker lacks a mechanism to **identify duplicates**.
7. **Duplicate Message Stored**
   - Broker **saves the duplicated record**.
   - Results in a **duplication problem**.

---

## At Least Once Semantics

- **Definition**
  - Messages are **not lost** because the producer **retries until** a success acknowledgement is received.
- **Implications**
  - May result in **duplicate messages** in the Kafka log.
- **Kafka's Default Behavior**
  - Kafka provides **At Least Once Semantics** by default due to the retry mechanism.

---

## At Most Once Semantics

- **Definition**
  - Messages are **sent only once**; no retries are performed.
- **How to Achieve At Most Once**
  - Configure the producer's **`retries` setting to zero**.
- **Implications**
  - **May lose some records** if transmission fails.
  - **No duplicate records** will be committed to the Kafka log.

---

## Summary

- **At Least Once Semantics**
  - **Ensures** messages are **not lost**.
  - **Duplicates may occur** due to retries.
  - Default behavior in Kafka.
- **At Most Once Semantics**
  - **No duplicates** are committed.
  - **Messages may be lost** if failures occur.
  - Achieved by setting **`retries` to zero**.

---

## Conclusion

- **Understanding Delivery Semantics**
  - Crucial to **choose the right semantics** based on application requirements.
- **Trade-offs**
  - **At Least Once**: Prioritizes **data integrity** over duplication.
  - **At Most Once**: Prioritizes **no duplication** over potential data loss.
- **Next Steps**
  - Evaluate whether **Exactly Once Semantics** is needed (not covered here).
  - Configure the producer settings according to the **needs of your application**.

---

**Note:** This mindmap includes all the information from the lecture, organized logically to ensure comprehensive understanding without missing any details.