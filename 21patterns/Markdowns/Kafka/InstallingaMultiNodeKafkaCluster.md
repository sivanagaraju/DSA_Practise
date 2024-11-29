# Mindmap: Setting up a Three-Node Kafka Cluster on a Local Machine

## Introduction

- **Objective**: Set up a three-node Kafka cluster on your local machine.
- **Kafka Version**: Using Confluent Community Edition (steps also apply to Open Source Kafka).
- **Prerequisites**:
  - Kafka binaries are downloaded and uncompressed.
  - No Kafka services are currently running.

## Preparation

- **Navigate to Kafka Home Directory**.
- **Locate the `server.properties` File** (Kafka broker configuration file):
  - **Confluent Kafka**: Found in `etc/kafka` directory.
  - **Open Source Kafka**: Found in `config` directory.
- **Purpose of `server.properties`**:
  - Contains broker configurations.
  - Supplied as an argument when starting the Kafka broker.
  - `kafka-server-start` command reads configurations from this file.

## Configuration for Multiple Brokers

- **Plan**: Start three Kafka brokers.
- **Steps**:
  1. **Create Copies of `server.properties`**:
     - Make three copies of the file.
     - Rename each copy to distinguish between brokers (e.g., `server-0.properties`, `server-1.properties`, `server-2.properties`).
  2. **Modify Each Configuration File**:
     - Ensure unique settings to prevent conflicts.

### Configurations to Modify

#### 1. Broker ID (`broker.id`)

- **Requirement**: Each broker must have a unique `broker.id`.
- **Modifications**:
  - **First Broker**: Leave `broker.id=0` (default).
  - **Second Broker**: Change to `broker.id=1`.
  - **Third Broker**: Change to `broker.id=2`.

#### 2. Listener Port (`port` or `listeners`)

- **Default Behavior**: Port configuration is commented out; broker uses default port `9092`.
- **Issue**: Multiple brokers on the same machine cannot share the same port.
- **Modifications**:
  - **Uncomment** the port configuration line.
  - **First Broker**: Set `port=9092`.
  - **Second Broker**: Set `port=9093`.
  - **Third Broker**: Set `port=9094`.
- **Note**:
  - In multi-machine setups, changing the port may not be necessary.

#### 3. Log Directory Location (`log.dirs`)

- **Purpose**: Directory where Kafka stores partition data.
- **Requirement**: Each broker should have its own log directory.
- **Modifications**:
  - **First Broker**: Set `log.dirs=/path/to/kafka-logs-0`.
  - **Second Broker**: Set `log.dirs=/path/to/kafka-logs-1`.
  - **Third Broker**: Set `log.dirs=/path/to/kafka-logs-2`.

#### 4. Other Configurations

- **Default Settings**: Other configurations can remain at default values.
- **Future Learning**: Additional configurations will be explored in later sections.

### Summary of Modifications

- **Three Key Configurations to Change**:
  1. **`broker.id`**: Ensure uniqueness.
  2. **`port`**: Assign different ports for brokers on the same machine.
  3. **`log.dirs`**: Set different log directories for each broker.
- **Alternative**:
  - For brokers on different machines, only `broker.id` needs to be unique.
  - Kafka can auto-assign `broker.id` (covered in another lesson).

## Starting the Kafka Cluster

### Cleaning Up Data Directories

- **Reason**: Remove previous data to start fresh.
- **Directories to Clean**:
  - **Kafka Log Directories**: As specified in `log.dirs`.
  - **ZooKeeper Data Directory**: Location specified in ZooKeeper configuration.
- **Caution**:
  - Deleting these directories will remove all past data.
  - Ensure this is intended before proceeding.

### Starting ZooKeeper

- **Requirement**: Kafka needs ZooKeeper to run.
- **Command**:
  ```bash
  bin/zookeeper-server-start.sh config/zookeeper.properties
  ```
- **Note**: Start ZooKeeper before starting Kafka brokers.

### Starting Kafka Brokers

- **Procedure**:
  - Open a new command window for each broker.
  - Use the respective configuration file for each broker.
- **Commands**:

  **First Broker**:
  ```bash
  bin/kafka-server-start.sh config/server-0.properties
  ```

  **Second Broker**:
  ```bash
  bin/kafka-server-start.sh config/server-1.properties
  ```

  **Third Broker**:
  ```bash
  bin/kafka-server-start.sh config/server-2.properties
  ```

- **Notes**:
  - The commands are the same except for the configuration file.
  - Ensure that each broker is started with its unique configuration.

### Running Multiple Brokers

- **Scalability**:
  - You can run as many brokers as desired on a single machine.
  - Each broker requires a unique configuration file with the necessary modifications.

## Additional Notes

- **Running Brokers on Separate Machines**:
  - Only the `broker.id` needs to be unique.
  - Ports and log directories do not need to be changed.
- **Auto-assigning Broker IDs**:
  - Kafka can be configured to auto-assign `broker.id`.
  - This feature will be discussed in a future lesson.
- **Cleaning Data Directories**:
  - Important for a fresh start.
  - Be cautious as this action is irreversible.
- **Default Configurations**:
  - Other configurations in `server.properties` are not conflicting.
  - They can remain at their default values unless specific changes are needed.

## Conclusion

- **Outcome**: Successfully set up a three-node Kafka cluster on a single machine.
- **Key Learnings**:
  - Modifying key configurations to avoid conflicts.
  - Understanding the importance of unique identifiers and resource allocation.
- **Next Steps**:
  - Explore additional configurations in later lessons.
  - Experiment with producing and consuming messages in the cluster.

---
