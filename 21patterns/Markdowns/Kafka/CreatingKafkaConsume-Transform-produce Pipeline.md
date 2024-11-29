# Kafka Consumers: Creating Kafka Consume-Transform-Produce Pipeline Mindmap

## Introduction

- **Recap of Previous Sections**
  - Learned extensively about **Kafka Producer APIs**.
  - Created multiple **producer examples**.
  - **Producers** are critical for originating and streaming data into the **Kafka cluster**.

- **Transition to Consumers**
  - Once data streams into Kafka, they can be **accessed** and **processed** by consumers.
  - Introduction to **stream processing applications** using Kafka.

## Stream Processing Tools Offered by Kafka

1. **Consumer APIs**
   - **Purpose**: Consume data from Kafka brokers and create stream processing applications.
   - **Focus of This Section**: Detailed introduction and practical implementation.

2. **Kafka Streams Library**
   - **Overview**: Client library for building applications and microservices.
   - **Note**: Beyond the scope of this beginner's course; requires separate training.

3. **KSQL (Kafka Query Language)**
   - **Overview**: SQL-like language for stream processing and real-time data analysis.
   - **Note**: Requires separate training; not covered in this course.

## Problem Statement

- **Objective**
  - Implement a miniature **real-time data validation service** for invoices.

- **Scenario**
  - Previously created a **POS Simulator** that generates invoices and sends them to a Kafka topic.
  - **New Requirement**: 
    - Read invoices in real-time.
    - Apply business rules to validate each invoice.
    - **Segregate** invoices based on validation:
      - **Valid Invoices**: Sent to a Kafka topic named `Valid Invoices`.
      - **Invalid Invoices**: Sent to a Kafka topic named `Invalid Invoices`.

- **Resulting System Overview**
  - **Valid Records**:
    - Consumed by a **data reconciliation application**.
    - Rectifies issues and sends back to the pool of valid records.
    - Consumed by other applications and microservices for business objectives.
  - **Invalid Records**:
    - Segregated for further processing and rectification.

## Starter Project

- **Included Components**
  - **Dependencies and Configurations**
    - `pom.xml`: Defines project dependencies.
    - `log4j2.xml`: Pre-configured logging.
  - **Scripts**
    - Start **ZooKeeper** and **Kafka services**.
    - Create Kafka topics.
  - **Predefined Java Packages**
    1. **`types` Package**
       - **Classes**:
         - `LineItem`: Defines the structure of a line item in the invoice.
         - `DeliveryAddress`: Defines the structure of an address.
         - `PosInvoice`: Combines invoice details, delivery address, and line items.
       - **Annotations**: Jackson annotations for serialization/deserialization.
       - **Generation**: Classes generated from schema definitions using **JSON schema to POJO Maven Plugin**.

    2. **`data_generator` Package**
       - **Classes**:
         - `AddressGenerator`: Provides random address data.
         - `ProductGenerator`: Provides random line item data.
         - `InvoiceGenerator`: Generates random `PosInvoice` objects using the above generators.

  - **Serialization Tools**
    - **JsonSerializer**: For serializing `PosInvoice` objects to JSON.
    - **JsonDeserializer**: For deserializing JSON messages back to `PosInvoice` objects.

  - **Configuration Class**
    - **`AppConfig`**: Contains configuration constants used across the application.

## Task Description

- **Objective**
  - Create a **multithreaded application** that:
    - Generates realistic invoices.
    - Sends them to a Kafka topic.
    - Implements a **consume-transform-produce** pipeline to validate and segregate invoices.

- **Requirements**
  - **Multithreaded Producer**
    - Create multiple **producer threads**.
    - Each thread uses `InvoiceGenerator.getNextInvoice()` to generate invoices.
    - Each thread sends the generated invoice to **Apache Kafka**.

  - **Data Validation Service**
    - Consume invoices from the input topic.
    - Apply **business rules** to validate invoices.
    - **Segregate** invoices:
      - Send **valid invoices** to `Valid Invoices` topic.
      - Send **invalid invoices** to `Invalid Invoices` topic.

## Creating the Kafka Consumer: Step-by-Step

### Step 1: Define Business Rules

- **Rule for Invalid Invoices**
  - An invoice is considered **invalid** if:
    - It is marked for **home delivery**.
    - **Contact number** for the delivery address is **missing**.

### Step 2: Set Up the Starter Project

- **Components**
  - **Dependencies and Configurations**: Already set up in the starter project.
  - **Predefined Classes**: `types` and `data_generator` packages.
  - **Serializer and Deserializer**: `JsonSerializer` and `JsonDeserializer`.
  - **Configuration Class**: `AppConfig`.

### Step 3: Create the Consumer Class

- **Main Class**: Create a class with the `main` method (e.g., `InvoiceValidator`).

#### Four-Step Process to Create a Kafka Consumer

1. **Create Java Properties and Set Consumer Configurations**
   - **Essential Configurations**:
     - `CLIENT_ID`: Unique identifier for the consumer.
     - `BOOTSTRAP_SERVERS`: Kafka broker addresses.
     - `KEY_DESERIALIZER`: Deserializer for the message key (e.g., `StringDeserializer`).
     - `VALUE_DESERIALIZER`: Deserializer for the message value (e.g., `JsonDeserializer`).
     - `VALUE_CLASS_NAME_CONFIG`: Target deserialized Java class (e.g., `PosInvoice.class`).
   - **Additional Configurations**:
     - **Consumer Groups**
     - **Offsets and Consumer Positions**: Covered in the next lecture.

2. **Create an Instance of `KafkaConsumer` Class**
   - **Type Parameters**:
     - Key: `String`
     - Value: `PosInvoice`
   - **Initialization**:
     - Pass the configured properties to the `KafkaConsumer` constructor.

3. **Subscribe to Kafka Topics**
   - **Subscription**
     - Subscribe to the **input topic** (e.g., `POS Invoices`).

4. **Read and Process Messages in an Infinite Loop**
   - **Polling**
     - Use the `poll` method with a timeout to retrieve records.
     - Example:
       ```java
       ConsumerRecords<String, PosInvoice> records = consumer.poll(Duration.ofMillis(100));
       ```
   - **Processing**
     - Iterate through each `ConsumerRecord`.
     - Apply **business rules** to determine validity.
     - **Segregate** and **produce** to respective topics.

### Step 4: Implement Data Validation Logic

- **Validation Criteria**
  - **Invalid Invoice**:
    - `DeliveryType` is `"HOME-DELIVERY"`.
    - `DeliveryAddress.ContactNumber` is **empty** or **missing**.
  - **Valid Invoice**:
    - Does not meet the invalid criteria.

- **Segregation Process**
  - **Valid Invoices**:
    - Send to `Valid Invoices` topic.
  - **Invalid Invoices**:
    - Send to `Invalid Invoices` topic.

### Step 5: Create a Producer for Segregated Invoices

- **Purpose**
  - To send validated invoices to respective Kafka topics based on validation.

- **Steps**
  1. **Create Producer Properties**
     - Similar to producer setup in earlier lectures.
     - **Serializer Configuration**: Use `JsonSerializer` since the data is JSON serialized.
  2. **Instantiate the Producer**
     - Create an instance of `KafkaProducer<String, PosInvoice>`.

  3. **Send Messages to Kafka Topics**
     - **Valid Invoices**:
       ```java
       ProducerRecord<String, PosInvoice> record = new ProducerRecord<>(VALID_TOPIC, invoice.getStoreID(), invoice);
       producer.send(record);
       ```
     - **Invalid Invoices**:
       ```java
       ProducerRecord<String, PosInvoice> record = new ProducerRecord<>(INVALID_TOPIC, invoice.getStoreID(), invoice);
       producer.send(record);
       ```

## Testing the Application

### Step 1: Prepare the Environment

- **Start Kafka Cluster Services**
  - Use provided scripts to start **ZooKeeper** and **Kafka brokers**.

### Step 2: Create Kafka Topics

- **Input Topic**: `POS Invoices` (if not already created).
- **Output Topics**:
  - `Valid Invoices`
  - `Invalid Invoices`

### Step 3: Run the POS Simulator

- **Load POS Simulator Application**
  - Use a separate IDE or terminal.
- **Execute the Simulator**
  - Generates and sends invoices to the `POS Invoices` topic.

### Step 4: Run the Invoice Validator Application

- **Start the Consumer Application**
  - Begins consuming invoices from `POS Invoices` topic.
  - Applies validation rules.
  - Segregates and produces to `Valid Invoices` or `Invalid Invoices` topics.

### Step 5: Verify the Results

- **Use Kafka Console Consumer**
  - **Check `Valid Invoices` Topic**:
    - Start a consumer to view messages:
      ```bash
      kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic Valid_Invoices --from-beginning
      ```
  - **Check `Invalid Invoices` Topic**:
    - Start a consumer to view messages:
      ```bash
      kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic Invalid_Invoices --from-beginning
      ```
  - **Expected Outcome**:
    - **Valid Invoices**: Should contain invoices that passed validation.
    - **Invalid Invoices**: Should contain invoices that failed validation based on the defined business rules.

## Summary of the Consume-Transform-Produce Pipeline

1. **Consume**
   - **Kafka Consumer** reads invoices from the `POS Invoices` topic.

2. **Transform**
   - **Data Validation**: Applies business rules to determine invoice validity.

3. **Produce**
   - **Kafka Producer** sends:
     - **Valid Invoices** to `Valid Invoices` topic.
     - **Invalid Invoices** to `Invalid Invoices` topic.

- **Pipeline Characteristics**
  - **Real-Time Processing**: Continuously consumes and processes invoices.
  - **Segregation**: Dynamically separates data based on validation outcomes.
  - **Scalability and Fault Tolerance**: Mentioned as future considerations.

## Important Considerations

- **Infinite Loop for Continuous Processing**
  - The consumer runs in an **infinite loop** to continuously process incoming data.
  
- **Consumer Groups and Offsets**
  - **Consumer Groups**: Manage how multiple consumers share the workload.
  - **Offsets**: Track the consumer's position in the topic.
  - **Note**: Detailed discussion on these topics will be covered in the next lecture.

- **Error Handling**
  - Handle potential exceptions during consumption and production to ensure **fault tolerance**.

- **Resource Management**
  - Ensure producers and consumers are properly **closed** on application shutdown to prevent resource leaks.

## Conclusion

- **Recap of Accomplishments**
  - Implemented a **Consume-Transform-Produce pipeline** using Kafka Consumers and Producers.
  - **Validated and segregated** invoices into **valid** and **invalid** categories.
  - Utilized **JSON serialization** for complex Java objects.

- **Next Steps**
  - **Upcoming Topics**:
    - **Consumer Scalability**: Strategies to scale consumer applications.
    - **Fault Tolerance**: Ensuring the consumer application handles failures gracefully.

- **Final Remarks**
  - "That's all for this session."
  - "See you in the next lecture."
  - **Keep learning and keep growing!**
  - **[Outro Music]**

---

**Note:** This mindmap comprehensively covers the lecture on introducing Kafka Consumers and creating a Consume-Transform-Produce pipeline using JSON serialized invoices. It includes problem statements, step-by-step implementation details, testing procedures, and important considerations for building robust Kafka consumer applications.