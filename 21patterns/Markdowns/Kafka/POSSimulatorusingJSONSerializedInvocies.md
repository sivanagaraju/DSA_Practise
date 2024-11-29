# Micro Project: Summing up the Producers - POS Simulator using JSON Serialized Invoices Mindmap

## Introduction

- **Recap**
  - In the earlier lecture, learned methods to scale Kafka producers.
- **Objective**
  - Create a more significant project: a Point of Sale (POS) Simulator.

## POS Simulator Overview

- **What is the POS Simulator?**
  - A producer that generates an **infinite number of random but realistic invoices**.
  - Sends invoices to the **Kafka broker**.
- **Command Line Arguments**
  1. **Topic Name**
     - Specifies which **Kafka topic** the producer should send all the invoices to.
  2. **Number of Producer Threads**
     - Specifies how many **parallel threads** to create for the application.
  3. **Producer Speed**
     - Specifies the **number of milliseconds** that each thread will wait between two invoices.
- **Example Calculation**
  - If you create **10 threads** with a **100 milliseconds** sleep time:
    - Each thread sends **10 messages per second**.
    - Total messages per second = 10 threads * 10 messages per thread = **100 messages per second**.
- **Purpose**
  - Generate a **specific workload** on your Kafka cluster.
  - Perform **load testing** and **monitoring**.
- **Note**
  - The **size of each message** is not being configured.
  - Application generates **JSON formatted, realistic invoices**.

## Starter Project

- **Included Components**
  - **Java Project Setup**
    - **`pom.xml`**
      - Defines **project dependencies**.
    - **`log4j2.xml`**
      - For **logging configuration**.
    - **Scripts**
      - Start **ZooKeeper** and **Kafka services**.
      - **Create Kafka topic**.
  - **Predefined Java Packages**
    - **1. `types` Package**
      - **Purpose**
        - Defines the **invoice structure** using Java classes.
      - **Classes**
        1. **`LineItem`**
           - Represents a **line item** in the invoice.
           - **Fields**:
             - `itemCode`
             - `itemDescription`
             - `price`
             - `quantity`
             - `totalValue`
        2. **`DeliveryAddress`**
           - Represents the **delivery address**.
           - **Fields**:
             - `addressLine`
             - `city`
             - `state`
             - `pinCode`
             - Other similar fields.
        3. **`PosInvoice`**
           - Represents the **POS invoice**.
           - **Fields**:
             - `invoiceNumber`
             - `createdTime`
             - `storeId`
             - `deliveryAddress` (object of `DeliveryAddress`)
             - `invoiceLineItems` (array of `LineItem` objects)
      - **Notes**
        - Classes are annotated with **Jackson annotations** for usage with **Jackson Data Bind Package**.
        - Classes were **generated from schema definitions** using **JSON schema to POJO Maven Plugin**.
    - **2. `data_generator` Package**
      - **Purpose**
        - Provides classes to **generate random data** for invoices.
      - **Classes**
        1. **`AddressGenerator`**
           - Method: `getNextAddress()`
             - Returns a **new random address**.
        2. **`ProductGenerator`**
           - Method: `getNextProduct()`
             - Returns a **random line item** for an invoice.
        3. **`InvoiceGenerator`**
           - Used by producer threads to **create random invoices**.
           - Method: `getNextInvoice()`

## Task Description

- **Objective**
  - Create a **multithreaded application** that generates invoices and sends them to a Kafka topic.
- **Requirements**
  - **Multithreaded Producer**
    - Create several **producer threads**.
    - Each thread uses `InvoiceGenerator.getNextInvoice()` to generate invoices.
    - Each thread sends the generated invoice to **Apache Kafka**.
- **Notes**
  - Similar to earlier examples where a multithreaded Kafka producer was created.
  - The challenge is now dealing with **complex Java objects** instead of plain string messages.

## Challenges and Considerations

- **Complex Java Objects**
  - The `PosInvoice` object has several fields of **different data types**.
    - Some fields are **`String`**.
    - Others are **`Integer`**, **`Number`**, **`Long`**.
  - **Nested Objects**
    - `DeliveryAddress` is an **object** within `PosInvoice`.
  - **Arrays of Objects**
    - `invoiceLineItems` is an **array** of `LineItem` objects.
- **Serialization**
  - Need to **serialize** the complex `PosInvoice` Java object before transmitting over the network.
  - Ensure that the serialized invoice can be **correctly deserialized** back into the `PosInvoice` Java object at the consumer.
- **Serializer Configuration**
  - A Kafka producer requires a **serializer configuration**.
  - Previously used `StringSerializer`, which is **not suitable** for complex objects.

## Serializer Options

- **Two Popular Alternatives in Kafka**
  1. **JSON Serializer and Deserializer**
     - **Advantages**
       - Easy to use.
       - JSON serialized objects are represented as **strings**.
       - Convenient for casting to strings and printing in **console** or **logs**.
       - Simplicity makes **debugging data issues** simple.
       - Commonly used and supported by many **data integration tools**.
     - **Disadvantages**
       - JSON serialized messages are **large in size**.
       - JSON format includes **field names** with each data element.
       - Field names increase the size of serialized messages by **2x or more**.
       - Causes more **delays at the network layer**.
  2. **AVRO Serializer and Deserializer**
     - **Advantages**
       - AVRO is a **binary format**.
       - Serialization is **much more compact**.
       - Messages are **shorter over the network**.
       - Provides more efficient **network bandwidth usage**.
     - **Disadvantages**
       - Not as straightforward for **debugging** and **logging** as JSON.
- **Decision for this Project**
  - Use **JSON Serializer**.
  - A **JSON Serializer class** is included in the **starter project**.
  - You can use this serializer in the example and in any other application where you want to serialize messages as JSON.

## Implementation Guidance

- **Your Task**
  - Implement the **POS Simulator**.
  - Generate invoices using `InvoiceGenerator`.
  - Send the invoices to a **Kafka topic**.
- **Approach**
  - Build on previous knowledge of implementing a **multithreaded Kafka producer**.
  - Handle serialization of complex Java objects using the provided **JSON Serializer**.
- **Support**
  - The **complete implementation source code** is included in the course material if you get stuck.
  - However, it's recommended to **write the code yourself** for learning purposes.

## Conclusion

- **Encouragement**
  - Start coding and apply what you've learned.
  - Hands-on practice is essential for mastering **Kafka producers** and **serialization**.
- **Closing Remarks**
  - "Good, that's all for this session."
  - "See you in the next lecture."
  - "**Keep learning and keep growing.**"
  - **[Outro Music]**

---