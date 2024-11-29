# Kafka ISR (In-Sync Replicas) Mindmap

## Introduction

- **Context**
  - Previously learned that followers continuously copy messages from the leader to stay in-sync.
  - This lecture focuses on the **ISR (In-Sync Replicas) list** in Kafka.

## Challenges in Keeping Followers In-Sync

- **Potential Issues with Followers**
  - Followers may fail to stay in-sync with the leader.
- **Common Reasons for Falling Behind**
  1. **Network Congestion**
     - Slows down replication.
     - Followers start falling behind due to delayed message transfers.
  2. **Broker Failures**
     - When a follower broker crashes:
       - All replicas on that broker begin falling behind.
       - Remain out of sync until the broker restarts and replication resumes.

## Leader's Responsibility: Maintaining the ISR List

- **What is the ISR List?**
  - **Definition**
    - A list of **In-Sync Replicas** (followers) for each partition.
  - **Purpose**
    - Tracks followers that are currently up-to-date with the leader.
  - **Storage**
    - Persisted in **ZooKeeper**.
  - **Maintained By**
    - The **leader broker** of each partition.

- **Importance of the ISR List**
  - **Critical for Cluster Health**
    - Ensures data consistency and availability.
  - **Leader Election**
    - Only followers in the ISR list are eligible to be elected as the new leader if the current leader fails.
    - Provides a set of reliable candidates for leadership.

## Determining if a Follower is In-Sync

- **How Does the Leader Know a Follower's Status?**
  - By monitoring the **offsets requested** by the follower.

- **Process of Monitoring Followers**
  1. **Follower Requests Messages**
     - Connects to the leader broker.
     - Requests messages starting from a specific **offset**.
  2. **Initial Request Example**
     - **First Request:** Starting from offset **0**.
     - **Leader's Response:** Sends messages from offset 0 to the latest (e.g., messages 0-9).
  3. **Follower Stores Messages**
     - Follower persists received messages into its replica.
  4. **Subsequent Requests**
     - **Next Request:** Starting from offset **10**.
     - Indicates the follower has successfully stored messages up to offset 9.
  5. **Leader's Inference**
     - By observing the last offset requested, the leader assesses how far the follower has progressed.
     - Determines if the follower is lagging or keeping pace.

## Maintenance of the ISR List

- **Dynamic Nature of the ISR List**
  - Followers are **added to** or **removed from** the ISR list based on their in-sync status.
  - The ISR list is continuously updated to reflect the current state of followers.

- **Criteria for Inclusion in the ISR List**
  - **"Not Too Far" Behind**
    - Followers must not be significantly lagging behind the leader.
    - A follower is considered in-sync if it stays within a defined lag threshold.

- **Leader's Actions Based on Follower Status**
  - **Adding to ISR**
    - If a replica is within the acceptable lag limit, it remains or is added to the ISR list.
  - **Removing from ISR**
    - If a replica falls beyond the acceptable lag, it is removed from the ISR list.

## Defining "Not Too Far" Behind

- **Understanding the Lag**
  - **Natural Delay**
    - Followers will always have some delay due to:
      - Requesting messages.
      - Network transmission times.
      - Writing messages to disk.
      - Preparing for the next request.
  - **Inevitable Lag**
    - A small lag is expected and acceptable.

- **Time Margin Allowed**
  - **Leader's Allowance**
    - The leader provides a time margin for followers to catch up.
  - **Default Lag Threshold**
    - **10 seconds** is the default value for the acceptable lag.
    - Configurable based on system requirements.

- **Configuring the Lag Threshold**
  - **Kafka Configuration**
    - The lag threshold can be adjusted using Kafka settings.
    - Allows for flexibility based on network conditions and performance needs.

## Criteria for Remaining in the ISR List

- **Conditions for Staying in the ISR**
  - A replica remains in the ISR list if it:
    - Has requested the most recent message within the last **10 seconds**.
    - Is not more than **10 seconds behind** the leader's latest offset.

- **Implications of Lagging Behind**
  - **Removal from ISR**
    - If a follower exceeds the lag threshold, the leader removes it from the ISR list.
  - **Re-adding to ISR**
    - Once the follower catches up and stays within the lag limit, it can be re-added to the ISR list.

## Importance of the ISR List for Fault Tolerance

- **Leader Failures**
  - In the event of a leader broker failure:
    - A new leader is elected from the ISR list.
    - Ensures the new leader has the most up-to-date data.
- **Data Consistency**
  - Replicas in the ISR list have nearly identical data to the leader.
  - Minimizes data loss during failover scenarios.
- **Cluster Reliability**
  - Maintaining an accurate ISR list enhances overall cluster stability and reliability.

## Conclusion

- **Summary of Key Points**
  - The ISR list is essential for tracking followers that are in-sync with the leader.
  - Leaders use the ISR list to determine eligible candidates for leadership in case of failure.
  - The ISR list is dynamic, with followers being added or removed based on their replication lag.
  - The acceptable lag threshold is typically **10 seconds** but can be configured.
  - Proper maintenance of the ISR list is crucial for Kafka's fault tolerance and high availability.

- **Final Remarks**
  - **Great, see you again. Keep learning and keep growing.**

---

