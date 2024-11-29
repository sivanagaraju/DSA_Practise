# Kafka Streams Mindmap

## Introduction

- **Kafka Big Picture for Beginners**
  - Lecture focuses on the **fourth component** of the Kafka ecosystem: **Kafka Streams**
  - **First three components** help create a simplified and manageable **data integration solution**
    - If data integration is all you need, you can stop after learning these
  - **Next two components** (including Kafka Streams) enable creating **scalable and fault-tolerant real-time stream processing applications**

- **Purpose of the Lecture**
  - Explain the **core concepts** of Kafka Streams
  - Provide answers to:
    1. **What is real-time stream processing?**
    2. **What is Kafka Streams and how does it solve stream processing challenges?**
    3. **How does Kafka Streams work?** *(Kafka Streams Architecture)*

---

## What is Real-Time Stream Processing?

### Definition of Data Streams

- **Unbounded, Infinite, Ever-Growing Sequences of Data**
  - Continuously generated and sent in small sizes (order of KBs)
  - Data streams are **unbounded**, meaning they **never end**

### Examples of Data Streams

- **Examples**
  - Sensors: Transportation vehicles, industrial equipment, healthcare devices, wearables
  - Log entries: Mobile apps, web apps, infrastructure components
  - Clickstreams: E-commerce, news sites, video streaming, gaming
  - Transactions: Stock market, credit card, ATMs, logistics
  - Social media, traffic activities, security systems
- **Observation**
  - **Everything** can be seen as a sequence of small data packets
  - Streams are **infinite** and **ever-growing**

### Challenges in Processing Data Streams

- **Traditional Approaches**
  1. **Collect and Store Data**, then:
     - **Query the Data**
       - **Request-Response Approach**
         - Handled through SQL
         - Asking **one question at a time** and getting quick answers
     - **Batch Processing**
       - Create big jobs to find answers to multiple queries
       - Scheduled to run at regular intervals (e.g., hourly, daily)
       - Asking a **bunch of questions at once** and repeating periodically
- **Stream Processing**
  - **Sits Between** request-response and batch processing approaches
  - **Continuous Process**
    - Ask a question **once**
    - System provides the **most recent version** of the answer **all the time**
  - **Continuously Updated Reports**
    - Updated based on data available up to that time
    - Reports **refresh** with new information as more data arrives
  - **Operations**
    - Joining streams, Grouping data, Computing aggregate
    - Similar to database queries and batch processing but done **continuously**

---

## Challenges of Using Databases for Stream Processing

  - **Complexity**
    - Databases and batch systems are not optimized for real-time processing.
    - Kafka Streams is designed specifically for stream processing.

---

## Why Can't We Use Kafka Producers, Consumers, and Kafka Connect?

- **Limitations for Stream Processing**
  - **Real-time stream processing** poses new challenges
  - **Kafka Producers, Consumers, and Connect** are designed for **data integration**
    - Not suitable for addressing stream processing problems
- **Need for Kafka Streams**
  - A tool **designed and developed** to meet stream processing requirements

---

## What is Kafka Streams and How Does It Solve Stream Processing Challenges?

### Kafka Streams Overview

- **Library for Building Applications and Microservices**
  - Input data are **streamed from Kafka topics**
    - Cannot use Kafka Streams without Kafka topics
  - Starting point is **one or more Kafka topics**

- **Powerful Features as a Simple Library**
  - **Standard Java and Scala Applications**
    - Perform real-time stream processing
  - **Flexible Deployment**
    - Any machine, virtual machine, container, or Kubernetes cluster
  - **Inherent Capabilities**
    - Parallel Processing, Fault Tolerance, Scalability
  - **Out-of-the-Box Capabilities**
    - Provided by the Kafka Streams library without extra configuration

### Critical Capabilities of Kafka Streams

- **Working with Streams and Tables**
  - **Interoperability**
    - Mix and match streams and tables in solutions
    - Convert a **stream to a table** and **vice versa**
- **Grouping and Aggregation**
  - **Group Streams**
    - Compute **continuously updating aggregates**
- **Joining Data**
  - **Join Streams**
  - **Join Tables**
  - **Join Streams and Tables**
- **State Management**
  - **Local State Stores**
    - Create and manage **fault-tolerant** and **efficient** state stores
- **Windowing and Time Management**
  - **Create Windows**
    - Different types (e.g., tumbling, hopping, sliding)
  - **Handle Time Complexities**
    - **Event Time** vs. **Processing Time**
    - **Late Arrivals (Latecomers)**
    - **High Watermark**
    - **Exactly-Once Processing**
- **Interactive Queries**
  - **Serve Other Microservices**
    - Using **request-response interface** over the streams application
  - Known as **Kafka Streams Interactive Query**
- **Testing Tools**
  - Provides tools for **unit testing** applications
- **Domain-Specific Language (DSL)**
  - **Easy-to-Use DSL**
    - For defining stream processing logic
  - **Custom Processors**
    - Flexibility to extend beyond provided functions
- **Fault Tolerance and Scalability**
  - **Inherent Fault Tolerance**
    - Automatic handling of failures
  - **Dynamic Scalability**
    - Scale applications as needed
- **Deployment in Containers and Kubernetes**
  - **Containerization**
    - Deploy applications in containers
  - **Kubernetes Cluster Management**
    - Manage applications within Kubernetes

- **Note**
  - The list of capabilities is **not exhaustive**

---

## How Does Kafka Streams Work? (Kafka Streams Architecture)

### Overview

- **Continuous Data Consumption**
  - Reads data from **one or more Kafka topics**
- **Application Logic**
  - Process streams **in real time**
  - **Take necessary actions** based on processed data

### Example Scenario

- **Application Deployment**
  - Deployed on a **single machine**
- **Input Topics**
  - Consuming from **two topics**: **T1** and **T2**
    - Each has **three partitions**
- **Application Functionality**
  - Could be monitoring:
    - **Traffic data**
    - **Patient vitals**
  - **Continuously checking thresholds**
    - Sending **alerts** when thresholds are breached

### Scalability and Fault Tolerance

- **Logical Tasks Creation**
  - Kafka Streams creates **three logical tasks**
    - Based on the **maximum number of partitions** (three)
  - **Automatic Task Creation**
    - No need for manual coding
- **Partition Assignment**
  - **Partitions Assigned to Tasks**
    - Partitions allocated **evenly** among tasks
    - Each task processes **one partition** from each topic
    - **Total of two partitions per task**
- **Thread Assignment**
  - **Configure Application Threads**
    - E.g., configure to run with **two threads**
  - **Task Distribution**
    - Kafka assigns tasks to threads
    - **Uneven Distribution**
      - One thread may handle **two tasks**
      - The other handles **one task**
    - **Performance Consideration**
      - Thread with two tasks might run slower
    - **All Data Gets Processed**
      - Despite uneven distribution
- **Multi-Threaded Configuration**
  - **Set Number of Max Threads**
    - Simple configuration change
    - Transforms application into a **multi-threaded** one
- **Scaling Out**
  - **Adding Instances**
    - Start another instance on a **different machine**
  - **Task Reassignment**
    - **New Thread (T3)** created
    - **One task migrates** to the new thread automatically
    - **Partitions and State Stores** migrate as well
  - **Workload Rebalancing**
    - Kafka Streams **rebalances** workload among instances
    - **Granularity** at the Kafka topic **partition level**
  - **Automatic and Seamless**
    - No need to stop or restart the application
- **Adding More Instances Beyond Task Count**
  - **Overprovisioning**
    - Additional instances remain **idle**
  - **Reason**
    - Number of tasks equals number of **available input partitions**
- **Fault Tolerance**
  - **Instance Failure Handling**
    - If an instance dies, Kafka Streams **automatically restarts** tasks on remaining instances
  - **Transparent Failure Handling**
    - Managed by the framework
    - **No user intervention required**

### Key Kafka Streams Concepts

- **Task Creation**
  - Logical tasks based on input topic partitions.
  - Maximum number of tasks equal to the maximum number of partitions across topics.
- **Thread Allocation**
  - Threads process tasks in parallel.
  - Uneven thread distribution when threads are fewer than tasks.
- **Scaling Out**
  - Adding new instances increases threads, redistributes tasks.
- **Fault Handling**
  - Transparent to the end user, managed by Kafka Streams framework.

---

## Conclusion

- **Kafka Streams Summary**
  - A tool **specifically designed** for real-time stream processing
  - Provides **scalability**, **fault tolerance**, and **ease of deployment**
  - Handles complexities unique to stream processing
- **Encouragement**
  - **Keep learning and keep growing**

---