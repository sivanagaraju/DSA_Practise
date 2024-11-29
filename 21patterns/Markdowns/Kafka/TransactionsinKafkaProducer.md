# Transactions in Kafka Producer Mindmap

## Introduction

- **Recap**
  - Previously learned about the **Idempotent Producer**.
- **Objective**
  - Introduce another advanced producer concept: the **Transactional Producer**.

---

## Transactional Producer Overview

- **Definition**
  - The **Transactional Producer** provides **transactional guarantees** in Kafka.
- **Atomicity**
  - Ability to **write to several partitions atomically**.
  - **Meaning**: Either **all messages** within the same transaction are committed, or **none** of them are saved.
  - Similar to atomicity in databases.

---

## Implementing Transactions: Example Scenario

### Preparation

- **Use Case**
  - Modify the existing **HelloProducer** example to implement transactions.
- **Setup**
  - Previously, we had one topic and sent messages to it.
  - Now, we will:
    - **Create two topics**:
      - `hello-producer-1`
      - `hello-producer-2`
    - Implement a transaction that sends messages to both topics.

### Transaction Behavior

- **Commit Transaction**
  - Messages are delivered to **both topics**.
- **Abort/Rollback Transaction**
  - Messages are **not sent** to any of the topics.
- **Goal**
  - Demonstrate atomicity by ensuring messages are either fully committed or not sent at all.

---

## Topic-Level Configurations for Transactions

- **Mandatory Configurations**
  - All topics included in a transaction must have:
    - **Replication Factor**: At least **3**.
    - **Minimum In-Sync Replicas (`min.insync.replicas`)**: At least **2**.
- **Verification**
  - Check the `create-topic` script:
    - Confirm replication factor is set to **3**.
    - Add `min.insync.replicas=2` to the topic configuration.

---

## Modifying the Application (`AppConfigs` Class)

- **Adjust Number of Events**
  - Reduce the number of events to **2** for easier verification.
- **Define Topic Names**
  - Create constants for both topic names:
    - `topicName1`
    - `topicName2`
- **Add Transaction ID**
  - Define a constant `transaction_id` to set `TRANSACTIONAL_ID_CONFIG` for the producer.

---

## Setting `TRANSACTIONAL_ID_CONFIG`

- **Mandatory for Transactions**
  - Setting a `transactional.id` is required to implement producer transactions.
- **Key Points**

  1. **Idempotence is Automatically Enabled**
     - When `transactional.id` is set, **idempotence** is automatically enabled.
     - Transactions depend on idempotence.

  2. **Unique Transactional ID per Producer Instance**
     - `TRANSACTIONAL_ID_CONFIG` must be **unique** for each producer instance.
     - **Cannot run multiple producer instances with the same `transactional.id`**.
     - If duplicated, one of the transactions will be **aborted** because it's illegal to have two instances with the same transactional ID.

- **Purpose of `transactional.id`**
  - Allows the broker to **roll back older unfinished transactions** in case of producer restarts or failures.
- **Scaling Considerations**
  - For horizontal scalability:
    - Each producer instance should have its **own unique `transactional.id`**.
    - All can send data to the same topic but will have different transactions.

---

## Implementing Transactions in the Producer

### Three-Step Process

1. **Initialize Transactions**

   - Call `producer.initTransactions()`.
   - **Purpose**:
     - Ensures any previous transactions with the same `transactional.id` are **completed or aborted**.
     - Retrieves an internal `producer_id` used in future messages.
     - The `producer_id` is used by the broker to implement idempotence.

2. **Begin and Commit Transactions**

   - **Begin Transaction**:
     - Call `producer.beginTransaction()`.
   - **Send Messages**:
     - Wrap all `send` API calls between `beginTransaction()` and `commitTransaction()`.
   - **Commit Transaction**:
     - Call `producer.commitTransaction()`.
     - All messages sent within this block are part of a **single transaction**.

3. **Handle Exceptions**

   - In case of an unrecoverable exception:
     - Call `producer.abortTransaction()`.
   - **Finally**:
     - Close the producer instance.

---

## Modifying the Code

- **Sending Messages to Both Topics**
  - Duplicate the `send` method call to send messages to both `topicName1` and `topicName2`.
- **Transaction Blocks**

  1. **First Transaction (Commit)**
     - Begin transaction.
     - Loop runs twice:
       - Sends one message to each topic in each iteration.
     - Commit transaction.
     - Messages should appear in both topics.

  2. **Second Transaction (Abort)**
     - Begin transaction.
     - Loop runs twice:
       - Sends one message to each topic in each iteration.
     - **Abort transaction** instead of committing.
     - Messages should **not appear** in any topic.

- **Logging**
  - Add log entries to monitor transaction start, commit, and abort.

---

## Testing the Implementation

### Steps

1. **Start Cluster Services**
   - Start Zookeeper and Kafka brokers.
   - Ensure both topics are created with the correct configurations.

2. **Execute the Application**
   - Run the modified `HelloProducer` application.
   - Observe the logs:
     - First transaction committed.
     - Second transaction aborted.

3. **Verify Results**
   - Use Kafka console consumer script to read messages from both topics.
   - **Expected Outcome**:
     - Only messages from the **first transaction** (tagged as T1) should be visible.
     - No messages from the **second transaction** (tagged as T2) should appear.

---

## Important Notes on Transactions

- **Single Open Transaction**
  - The same producer **cannot have multiple open transactions** simultaneously.
  - Must **commit or abort** the current transaction before starting a new one.

- **Commit Transaction Behavior**
  - `commitTransaction()` will **flush any unsent records** before committing.
  - If any `send` calls failed with an **irrecoverable error**:
    - `commitTransaction()` will **throw an exception**.
    - You are supposed to **abort the whole transaction**.
  - Aligns with the principle: **"All or Nothing"**.

- **Multithreaded Producer Implementation**
  - When using multiple threads:
    - Call `beginTransaction()` **before starting threads**.
    - **Commit or abort** the transaction **after all threads complete**.

---

## Conclusion

- **Summary**
  - Demonstrated how to implement transactions in Kafka producer.
  - Showed how transactions ensure atomicity across multiple topics.

