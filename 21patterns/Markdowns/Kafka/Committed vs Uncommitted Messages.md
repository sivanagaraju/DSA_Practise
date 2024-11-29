# Committed vs Uncommitted Messages in Kafka Mindmap

## Introduction

- **Welcome Back**
  - Continuing from previous discussions on Kafka's ISR (In-Sync Replicas) list.
- **Objective**
  - Understand the concepts of **committed** and **uncommitted** messages.
  - Learn how Kafka handles potential message loss due to ISR dynamics.

## Challenges with ISR Maintenance

- **ISR Mechanism**
  - **Fancy but has a Gotcha**
    - Followers may lag behind the leader for various reasons.
    - Lagging followers can be removed from the ISR list.

- **Reasons for Followers Lagging**
  - **Network Congestion**
    - Slows down replication, causing followers to fall behind.
  - **Broker Failures**
    - When a follower broker crashes, its replicas stop updating until it restarts.

- **Scenario: All Followers Lagging**
  - **Assumption**
    - All followers in the ISR list are **11 seconds** behind the leader.
    - ISR threshold is **10 seconds**.
  - **Result**
    - None of the followers qualify to be in the ISR.
    - **ISR List Becomes Empty**.
    - Messages are only present at the leader.

- **Leader Failure Risk**
  - **If the Leader Crashes**
    - Need to elect a new leader from followers not in the ISR.
  - **Problem**
    - Risk of losing messages collected at the leader during the last **11 seconds**.
    - These messages haven't been replicated to followers.

## Solutions to Prevent Message Loss

### 1. Introduce Committed and Uncommitted Messages

- **Concept Overview**
  - **Committed Messages**
    - Messages that have been safely replicated to all replicas in the ISR list.
  - **Uncommitted Messages**
    - Messages not yet replicated to all ISR followers.

- **Leader Configuration**
  - Configure the leader **not to consider a message committed** until it's copied to **all followers in the ISR**.
  - This leads to the leader having both committed and uncommitted messages.

- **Implications**
  - **Committed Messages**
    - Safe from loss unless all replicas fail.
  - **Uncommitted Messages**
    - At risk if the leader fails before replication.

- **Message Commitment Process**
  1. **Producer Sends Message** to the leader.
  2. **Leader Writes Message** to its local log.
  3. **Leader Replicates Message** to followers in the ISR.
  4. **Once All ISR Followers Acknowledge**, the message is marked as **committed**.
  5. **Leader Sends Acknowledgment** to the producer.

### 2. Set a Minimum In-Sync Replicas Configuration

- **Minimum ISR Setting**
  - **Definition**
    - A configuration parameter that specifies the minimum number of ISR replicas required for a message to be considered committed.
  - **Purpose**
    - Ensures that messages are only committed when there are enough replicas to safely store them.

- **Behavior When ISR Falls Below Minimum**
  - **Leader Actions**
    - Stops acknowledging new messages as committed.
    - May stop accepting writes if configured to do so.
  - **Producer Impact**
    - Producers may receive errors or timeouts.
    - Encourages producers to retry or handle the situation appropriately.

- **Benefits**
  - **Data Safety**
    - Prevents the system from acknowledging messages that aren't safely replicated.
  - **Consistency**
    - Ensures that committed messages have the desired replication level.

## Handling Uncommitted Messages

- **Producer's Role**
  - **Acknowledgment Configuration**
    - Producers can choose to wait for acknowledgments only after messages are fully committed.
    - **Acknowledgment Levels (acks)**
      - `acks=all`: Producer waits for full commit acknowledgment.
  - **Timeout and Retries**
    - Producer waits for an acknowledgment within a timeout period.
    - If no acknowledgment, the producer **resends** the messages.

- **Recovery from Leader Failure**
  - **Uncommitted Messages Lost**
    - If the leader fails before messages are committed, those messages are lost.
  - **Resending Messages**
    - Producers resend uncommitted messages.
    - **New Leader Receives Messages**
      - Newly elected leader processes the resent messages.
  - **Message Protection**
    - Ensures all messages are eventually committed despite failures.

## Summary

- **Key Points**
  - **ISR List Dynamics**
    - Followers can be removed from the ISR if they fall behind.
    - An empty ISR list poses a risk for message loss upon leader failure.
  - **Committed vs Uncommitted Messages**
    - Committed messages are replicated to all ISR followers and are safe.
    - Uncommitted messages reside only on the leader and are at risk.
  - **Minimum ISR Configuration**
    - Helps ensure messages are only committed when adequately replicated.
  - **Producer's Strategy**
    - By waiting for full acknowledgments, producers can detect uncommitted messages and resend them if necessary.

- **Conclusion**
  - These mechanisms collectively help prevent message loss in Kafka.
  - Understanding these concepts is crucial for designing reliable data streaming applications.

- **Next Steps**
  - These ideas will be revisited with practical examples later in the course.
  - Further exploration will solidify understanding through hands-on experience.

## Closing Remarks

- **Encouragement**
  - If the concept isn't entirely clear now, it will become clearer with examples.
  - **Keep Learning and Keep Growing**

---

