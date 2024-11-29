# Working with Types and Serialization in Kafka Mindmap

## Introduction

- **Recap of Previous Section**
  - Learned how to create **Kafka Producers**.
  - Sent data to the **Kafka Cluster**.
- **Current Challenge**
  - Previously sent **simple text messages**.
  - **Real-life records** are not plain text or string messages; they are **complex Java objects**.

## Challenges in Kafka Programming

- **Dealing with Data Records in Various Formats**
  - Kafka programming mainly deals with **data records** in a **variety of formats**.
- **Two Critical Questions**
  1. **How to Create Java Types**
  2. **How to Serialize Your Java Types for Sending Them to Kafka**

## Issues with Manual POJO Creation

- **Simple Examples**
  - Can manage with **4 or 5 types**.
- **Real-Life Scenarios**
  - Complex data processing requirements can quickly scale up to **hundreds of unique record formats**.
- **Problem**
  - Creating **Plain Old Java Objects (POJOs)** for message types is a **tedious mechanical activity**.
- **Solution**
  - **Automate** the creation of Java types.

## Automating Java Type Creation

- **Goal**
  - Define a **message schema** using a simple schema definition language.
  - Use an **IDE** or **build tool** to generate Java class definitions from the schema **automatically**.
- **Available Tools and Methods**
  - There are many ways and several tools to help achieve this.
- **Two Alternatives for Kafka Applications**
  1. **JSON Schema to POJO**
     - Define message schema using **JSON Schema**.
     - Generate POJOs from JSON Schema.
  2. **Avro Schema to POJO**
     - Define message schema using **Avro Schema Definition Language**.
     - Generate POJOs from Avro Schema.
- **Open Source Support**
  - Enough open-source support for generating POJOs for both options.
- **Plan**
  - Cover one example for each format: **JSON** and **Avro**.

## Serialization and Deserialization

- **First Half of the Problem**
  - **Generating POJOs**.
- **Second Half of the Problem**
  - **Serializing and Deserializing** the Java types.
- **Requirement**
  - Provide a **Serializer** and a **Deserializer** for all Java types used in the Kafka application.
- **Challenges**
  - Creating a serializer for each kind is a **big headache**.
- **Solution**
  - Develop **reusable serializers and deserializers**.
  - Apply the same to **all Java types**.

## Common Object Serialization Formats

- **Options for Kafka Applications**
  - Many object serialization formats exist.
- **Two Most Commonly Used Formats**
  1. **JSON Serialization**
     - Use **JSON format** to serialize Java objects.
  2. **Avro Serialization**
     - Use **Avro format** to serialize Java objects.

## Learning Objectives

- **In This Section, We Will Learn**
  1. **Defining Schema Using JSON**
     - How to define the **schema of events** using JSON.
     - How to **auto-generate** a serializable POJO definition from the JSON schema definition.
  2. **Defining Schema Using Avro**
     - How to define the **schema of events** using **Avro Schema Definition Language**.
     - How to **auto-generate** a serializable POJO definition from the Avro schema definition.
- **Next Section**
  - How to **Serialize** these objects using **JSON** as well as **Avro Serialization**.

