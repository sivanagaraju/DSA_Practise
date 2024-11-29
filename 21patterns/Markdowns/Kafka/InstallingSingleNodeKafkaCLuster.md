# Kafka Setup Mindmap

## Overview

- **Introduction**
  - Setting up a **Single Node Kafka** on your local machine
  - Contextual theory before the setup
- **Kafka Flavors and Categories**
  - Kafka comes in many flavors, classified into three categories:
    1. **Open Source Version of Kafka**
    2. **Commercial Distribution**
    3. **Fully Managed Kafka Service in the Cloud**

## Kafka Flavors Explained

### 1. Open Source Version of Kafka

- **Description**
  - Downloadable from the Apache website
  - You can install, use, and manage it yourself
- **Challenges**
  - Operational issues or open bugs
  - Need to upgrade Kafka versions
  - Infrastructure problems
- **Considerations**
  - Requires in-house expertise to handle issues
  - Organizations are unlikely to use this unless they have Kafka admins and infrastructure experts
  - It's hard to find skilled professionals who understand the ins and outs of Kafka clusters

### 2. Commercial Distribution

- **Description**
  - Comes with tools and utilities to manage daily operations and monitor your cluster
  - Vendor provides trained and highly skilled support professionals
- **Examples**
  - **Confluent Kafka**
    - Most popular commercial distribution
    - Offers a **Community Edition** without any cost (used in this course)
- **Benefits**
  - Easier cluster management
  - Professional support for operational issues
- **Considerations**
  - Comes at a cost to your organization
  - Most likely setup in production environments

### 3. Fully Managed Kafka Service in the Cloud

- **Description**
  - No need to download, install, run, operate, or maintain the Kafka cluster
  - Use the cluster for producing and consuming data
  - Infrastructure is managed by the service provider
- **Examples**
  - **Confluent Cloud**
  - **Amazon Managed Streaming for Kafka (MSK)**
  - **Aiven Kafka**
- **Benefits**
  - Simplest way to use Kafka for projects
  - Different payment plans available
- **Considerations**
  - All these options provide a Kafka cluster, but you still need to develop applications for creating and processing data streams

## Setting Up Confluent Kafka Community Edition

### Download and Installation

- **Steps**
  1. Go to **[confluent.io](https://www.confluent.io/)**
  2. Click on the **Download** button
  3. Scroll down to find the link to download the **Community Edition**
  4. Uncompress the downloaded file
- **Result**
  - You will see a directory containing a preconfigured single-node Kafka cluster

### Prerequisites

- **Java Installation**
  - Kafka is a JVM-based application
  - Ensure Java is installed on your machine
  - Check Java installation using the command:
    ```bash
    java -version
    ```

### Kafka Command Line Tools

- **Location**
  - Found in the `bin` directory of your Kafka installation
- **Scripts**
  - **Shell Scripts**: For Linux or Mac (`bin` directory)
  - **Windows Batch Files**: For Windows (`bin\windows` directory)
- **Usage**
  - Use the appropriate scripts based on your operating system

## Starting a Single Node Kafka Cluster

### Overview

- **Process**
  - Starting a Kafka cluster is a two-step process:
    1. Start the **ZooKeeper server**
    2. Start the **Kafka broker**

### Step 1: Start ZooKeeper Server

- **Command**
  - Use the `zookeeper-server-start` script
  - Requires one mandatory argument: the ZooKeeper configuration file
- **Configuration File**
  - Located at `etc/kafka/zookeeper.properties` (Confluent Kafka)
- **Possible Issue on Windows**
  - **Broken Script Fix**
    - If you encounter an error, the Confluent Kafka download may have a broken script for Windows
    - **Fix Steps**:
      1. Open the file `bin\windows\kafka-run-class.bat`
      2. Search for the text `'Classpath addition for the core'`
      3. Copy and paste the following content above the selected line:
         ```batch
         REM Classpath addition for core
         for %%i in ("%BASE_DIR%\libs\*") do (
           call :concat "%%i"
         )
         ```
      4. Save the file
      5. Run the ZooKeeper server again
- **Running ZooKeeper**
  - Once fixed, ZooKeeper should start and run without issues

### Step 2: Start Kafka Broker

- **Command**
  - Use the `kafka-server-start` script
  - Requires a configuration file
- **Configuration File**
  - Located at `etc/kafka/server.properties` (Confluent Kafka)
- **Execution**
  - Open a new command window
  - Run the script with the configuration file
- **Confirmation**
  - Look for the message `[KafkaServer id=0] started`
  - Indicates that your Kafka broker is running with ID 0

## Understanding ZooKeeper

- **What is ZooKeeper?**
  - A kind of database where Kafka brokers store shared information
  - Used as a shared system among multiple Kafka brokers
  - Coordinates various tasks among brokers
- **Role in Kafka**
  - Essential for coordinating things among brokers
  - Must be running even if you have a single broker
- **Future Plans**
  - Kafka community plans to retire ZooKeeper in future versions
  - Until then, ZooKeeper remains a necessary component

## Using Open Source Apache Kafka

### Introduction

- **Option**
  - You can also use the open-source edition of Kafka
- **Steps**
  - Similar to Confluent Kafka with minor differences

### Shutting Down Existing Kafka Instance

- **Reason**
  - To avoid port conflict issues
- **Steps**
  - Close the command windows running ZooKeeper and Kafka broker

### Download and Installation

- **Steps**
  1. Go to the **[Apache Kafka website](https://kafka.apache.org/)**
  2. Click on the **Download** button
  3. Choose a binary download (e.g., with Scala 2.13)
  4. Uncompress the downloaded file
- **Directory Structure**
  - Similar to Confluent Kafka but with some differences
  - Some directories may be missing
  - Core functionalities remain the same
- **Note**
  - Confluent Kafka includes additional capabilities

### Starting ZooKeeper and Kafka Broker

#### Start ZooKeeper

- **Command**
  - Use the `zookeeper-server-start` script
  - Configuration file location may differ (e.g., `config\zookeeper.properties`)
- **Example Command (Windows)**
  ```batch
  bin\windows\zookeeper-server-start.bat config\zookeeper.properties
  ```
- **Confirmation**
  - ZooKeeper should start and listen on port **2181**

#### Start Kafka Broker

- **Command**
  - Use the `kafka-server-start` script
  - Configuration file location may differ (e.g., `config\server.properties`)
- **Example Command (Windows)**
  ```batch
  bin\windows\kafka-server-start.bat config\server.properties
  ```
- **Confirmation**
  - Kafka broker should start successfully

## Next Steps

- **Ready to Use Kafka**
  - With ZooKeeper and Kafka broker running, you can start using Kafka for hands-on activities
- **Exploring Managed Services**
  - If interested, explore Kafka managed services like:
    - **Confluent Cloud**
    - **Aiven Kafka**

## Conclusion

- **What We Learned**
  - How to start a single-node Kafka broker using:
    - **Confluent Community Edition**
    - **Open Source Apache Kafka**
  - Importance of ZooKeeper in Kafka's architecture
- **Key Takeaways**
  - Regardless of the distribution, core steps to start Kafka are similar
  - Understanding different Kafka options helps in choosing the right setup for your needs
- **Encouragement**
  - Continue learning and experimenting with Kafka
  - Stay tuned for more advanced topics in upcoming lectures

---
