# Kafka Connect Mindmap

## Overview

- **Kafka Ecosystem Core Components**
  - Kafka Brokers
  - Kafka Producers
  - Kafka Consumers
  - **Kafka Connect** (focus of this lecture)

- **Data Integration Problem in Enterprises**
  - **Multiple Independent Applications**
    - Custom-designed in-house applications
    - Third-party vendor applications
    - External systems maintained by partners or service providers
  - **Need for Data Sharing Across Systems**
    - Applications generate and own data
    - Require data from other systems for operations
  - **Examples of Data Integration Needs**
    - Financial accounting software needs data from invoicing system
    - Inventory management system needs data from invoicing, warehouse, and shipment systems
    - Analytics requires data from across the enterprise
  - **Complexity of Data Pipelines**
    - Messy network of point-to-point data pipelines
    - Difficult to maintain and scale
  - **Kafka as a Solution for Simplifying Data Pipelines**
    - Kafka Broker acts as a central data hub
    - One-to-one pipelines to Kafka instead of many-to-many between applications
    - Reduces workload on source applications
    - Simplifies data integration and maintenance

## What is Kafka Connect?

- **Definition**
  - Kafka Connect is a component of Kafka for connecting and moving data between Kafka and external systems.
  - Provides out-of-the-box data integration without writing code.

- **Use Cases**
  - Ingest data from source systems into Kafka (e.g., databases, file systems)
  - Export data from Kafka to target systems (e.g., data warehouses, NoSQL databases)

- **Source and Sink Connectors**
  - **Source Connector**
    - Pulls data from an external source system and sends it to Kafka
    - Internally uses Kafka Producer API
  - **Sink Connector**
    - Consumes data from Kafka topics and writes it to an external target system
    - Internally uses Kafka Consumer API

- **Alternatives to Kafka Connect**
  - **Embedded Producer in Source Application**
    - Modify source application to include Kafka Producer code
    - Not practical if source code is unavailable or modification is infeasible
  - **Independent Kafka Producer**
    - Create a standalone producer to read from the source and write to Kafka
    - Requires custom code development
  - **Using Kafka Connect**
    - No code required
    - Configure and run pre-built connectors
    - Simplifies data integration tasks

## How Do They Provide Out-of-the-Box Source and Sink?

- **Kafka Connect Framework**
  - A framework for developing connectors
  - Open-sourced and allows community contributions
  - Handles heavy lifting: scalability, fault tolerance, error handling

- **Connector Development**
  - Implemented in Java
  - Two main classes to implement:
    - **SourceConnector** or **SinkConnector**
    - **SourceTask** or **SinkTask**
  - Developers focus on:
    - How to split data for parallel processing (Connector class)
    - How to interact with external systems (Task class)
  - Package connectors as JARs or ZIP archives for distribution

- **Availability of Pre-Built Connectors**
  - Developed by system vendors and the community
  - Examples of systems with connectors:
    - **Relational Databases** (e.g., JDBC Source Connector)
    - **Data Warehouses** (e.g., Snowflake Sink Connector)
    - **Cloud Storage** (e.g., Amazon S3, Hadoop HDFS)
    - **NoSQL Databases** (e.g., Cassandra, MongoDB)
    - **Messaging Systems** (e.g., MQTT, JMS)
    - **Social Media Platforms** (e.g., Twitter, Reddit)
    - **CRM Systems** (e.g., Salesforce)
    - **Others**: Elasticsearch, Google Firebase, local file systems

- **Using Connectors**
  - **Installation**
    - Download and install the appropriate connector
    - Ensure JAR files and dependencies are available to Kafka Connect workers
  - **Configuration**
    - Provide necessary information (e.g., connection details, data to transfer)
    - Configuration files or REST API
  - **Execution**
    - Run the connector
    - Kafka Connect handles data movement
    - No need to write custom code

## Can We Scale Kafka Connect?

- **Kafka Connect Cluster**
  - Composed of multiple **Connect Workers**
  - Workers can be added to increase capacity
  - Workers form a cluster using a **group ID** (similar to Kafka consumer groups)
  - Provides fault tolerance and load balancing

- **Scaling with Workers and Tasks**
  - **Workers**
    - Run on separate machines or processes
    - Act as containers for connectors and tasks
    - Manage the execution of connectors and tasks
  - **Tasks**
    - Units of work within a connector
    - Can be configured to parallelize data transfer
    - Example: One task per database table
  - **Dynamic Scaling**
    - Add or remove workers without stopping connectors
    - Workers automatically rebalance tasks among themselves

- **Running Multiple Connectors**
  - A single Kafka Connect cluster can run multiple connectors (both source and sink)
  - Example:
    - Source Connector for ingesting data from a database
    - Sink Connector for exporting data to Snowflake
    - Additional connectors (e.g., Salesforce Connector) can be added as needed

## Does It Merely Copy the Data? Can We Perform Some Processing or Transformations?

- **Single Message Transformations (SMTs)**
  - **Purpose**
    - Apply lightweight transformations to individual messages on the fly
  - **Examples of SMTs**
    - **Add Fields**
      - Add a new field with static data or metadata
    - **Modify Fields**
      - Filter out fields
      - Rename fields
      - Mask fields with null values
    - **Change Record Key**
      - Modify the key of the record
    - **Route Records**
      - Send records to different Kafka topics based on conditions
  - **Usage**
    - Configure SMTs in the connector configuration
    - Chain multiple SMTs for complex transformations

- **Limitations of SMTs**
  - Not suitable for complex data validations and transformations
  - Intended for simple, per-message changes
  - For complex processing, use Kafka Streams or external processing frameworks

## Kafka Connect Architecture: How Does It Work?

- **Key Components**
  - **Workers**
    - Main processes that form the Kafka Connect cluster
    - Run connectors and tasks
    - Handle Kafka interactions, error handling, and monitoring
    - Provide scalability, fault tolerance, and load balancing
  - **Connectors**
    - Define how to connect to external systems
    - Determine the degree of parallelism (number of tasks)
    - Do not directly move data; they manage tasks
  - **Tasks**
    - Perform the actual data transfer
    - Interact with external systems (read or write data)
    - Hand off data to workers (for source tasks)
    - Receive data from workers (for sink tasks)

- **Fault Tolerance and Load Balancing**
  - Workers detect failures of other workers
  - Reassign connectors and tasks as needed
  - Workers can be added or removed dynamically
  - Ensures high availability and reliability

- **Connector and Task Workflow**
  - **Installation**
    - Install connector JAR files and dependencies on all workers
  - **Configuration**
    - Provide settings like connection details, data to transfer, maximum tasks
    - Can be provided via configuration files or REST API
  - **Starting a Connector**
    - Workers start the connector process
    - Connector determines how to split work into tasks
    - Example: Splitting by tables, partitions, or other criteria
  - **Task Execution**
    - Tasks are assigned to workers for load balancing
    - **Source Tasks**
      - Connect to external sources
      - Read data at regular intervals
      - Hand over records to the worker
    - **Sink Tasks**
      - Receive records from the worker
      - Write data to external targets
    - Workers handle the interaction with the Kafka cluster
  - **Example Workflow**
    - **Source Connector Example**
      - Ingest data from five database tables
      - Connector creates five tasks (one per table)
      - Tasks read data and hand records to workers
      - Workers send records to Kafka topics
    - **Sink Connector Example**
      - Consume data from Kafka topics
      - Tasks write data to target systems (e.g., Snowflake)

- **Design Considerations**
  - **Reusable Design**
    - Separates external system interaction from Kafka interaction
    - External system interaction is handled by tasks
    - Kafka interaction is handled by workers
  - **Connector Developer's Responsibilities**
    - Implement splitting logic in the **Connector** class
    - Implement external system interaction in the **Task** class
  - **Kafka Connect Framework Responsibilities**
    - Handle interactions with Kafka
    - Manage configurations and distributions to tasks
    - Provide error handling and recovery
    - Monitor connectors and tasks
    - Scale up or down as needed

- **Fault Tolerance Mechanisms**
  - **Worker Failures**
    - Remaining workers detect failure
    - Reassign tasks from the failed worker
  - **Task Failures**
    - Workers can restart failed tasks
    - Error handling strategies can be configured

- **Scalability**
  - **Adding Workers**
    - Increases processing capacity
    - Tasks are rebalanced across workers
  - **Adjusting Tasks**
    - Configure the maximum number of tasks per connector
    - Increase tasks to parallelize data transfer
    - Limited by the connector's ability to split work

- **Dynamic Configuration**
  - **REST API**
    - Start, stop, and configure connectors using REST calls
    - Monitor connector status and metrics
  - **Configuration Changes**
    - Update connector configurations without downtime
    - Workers distribute new configurations to tasks

---

