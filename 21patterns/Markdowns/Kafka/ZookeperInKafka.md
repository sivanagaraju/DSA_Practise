# Kafka Broker Cluster and ZooKeeper Mindmap

## Introduction

- **Welcome Back**
  - Continuation of the previous lecture on Kafka clustering.
  - Focus on how Kafka maintains the list of active brokers using Apache ZooKeeper.

## Kafka Broker as a Masterless Cluster

- **Masterless Architecture**
  - Kafka does not follow a master-slave architecture.
  - All brokers operate as peers without a central master node.

- **Use of Apache ZooKeeper**
  - Kafka uses ZooKeeper to maintain coordination among brokers.
  - ZooKeeper keeps track of active brokers in the cluster.

## Broker Configuration and Unique IDs

- **Unique Broker ID**
  - Each Kafka broker has a unique ID defined in its configuration file.
  - The broker ID is essential for identification within the cluster.

- **ZooKeeper Connection Details**
  - Brokers specify ZooKeeper connection details in their configuration files.
  - Necessary for brokers to connect and register with ZooKeeper.

## Broker Registration with ZooKeeper

- **Creating an Ephemeral Node**
  - When a broker starts, it connects to ZooKeeper.
  - It creates an **ephemeral node** using its broker ID to represent an active session.
  - Example path: `/brokers/ids/[broker_id]`

- **Ephemeral Node Behavior**
  - The ephemeral node remains as long as the broker's session with ZooKeeper is active.
  - If the broker loses connectivity, ZooKeeper automatically removes the ephemeral node.

## Maintaining the List of Active Brokers

- **ZooKeeper's Role**
  - ZooKeeper maintains the list of active brokers as ephemeral nodes.
  - The list is stored under the path `/brokers/ids` in ZooKeeper.

- **Dynamic Updates**
  - Addition of a broker: A new ephemeral node is created.
  - Removal of a broker: The corresponding ephemeral node is deleted.

## Demonstration

### Connecting to ZooKeeper Shell

- **Starting ZooKeeper Shell**
  - Use the command to start the ZooKeeper shell:
    ```bash
    zkCli.sh -server [host]:[port]
    ```
  - Example: `zkCli.sh -server localhost:2181`

- **Navigating the ZooKeeper Hierarchy**
  - Use the `ls` command to list nodes:
    ```bash
    ls /
    ```
  - Shows top-level hierarchies.

### Viewing Active Brokers

- **Checking Brokers Node**
  - Navigate to the brokers directory:
    ```bash
    ls /brokers
    ```
- **Listing Broker IDs**
  - View active broker IDs:
    ```bash
    ls /brokers/ids
    ```
  - Output example: `[0, 1, 2]` indicating three active brokers.

### Simulating Broker Failure

- **Stopping a Broker**
  - Stop broker with ID 1 using appropriate command or script.
- **Observing ZooKeeper Changes**
  - In ZooKeeper shell, list broker IDs again:
    ```bash
    ls /brokers/ids
    ```
  - Broker ID 1 is no longer listed.

- **Restarting the Broker**
  - Start broker with ID 1 again.
- **Verifying Broker Re-registration**
  - List broker IDs:
    ```bash
    ls /brokers/ids
    ```
  - Broker ID 1 reappears in the list.

## Conclusion

- **Kafka's Broker List Maintenance**
  - Kafka uses ephemeral nodes in ZooKeeper to maintain the list of active brokers.
  - The list is dynamically updated as brokers join or leave the cluster.

- **Understanding Cluster Dynamics**
  - Brokers create ephemeral nodes upon startup, which are removed if they disconnect.
  - This mechanism ensures the cluster is aware of the current state of all brokers.

- **Closing Remarks**
  - This is how Kafka maintains the list of brokers in a cluster.
  - **Great, see you again. Keep learning and keep growing.**

---

