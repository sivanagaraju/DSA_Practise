# Using AVRO Schema Mindmap

## Introduction

- **Welcome Back**
  - Previously learned to work with **JSON serialization**.
- **Objective**
  - In this lecture, we will explore **AVRO serialization**.

---

## AVRO Overview

- **What is AVRO?**
  - AVRO is a **standard** widely accepted by the **big data community**.
  - Used extensively in **big data projects**.
- **Benefits of AVRO**
  - Can **quickly generate POJOs** from an AVRO schema.
  - Offers **similar simplicity** to JSON schema generation.

---

## Schema Remodeling Due to AVRO Limitations

- **Inheritance Limitation in AVRO**
  - **AVRO generated classes do not support inheritance**.
    - Cannot model Java `extends` and `implements` constructs.
- **Previous JSON Schemas**
  - In the JSON schema lecture, we created **four schema definitions**:
    1. **First Two Schemas**
       - Can be **perfectly converted** to AVRO.
    2. **Other Two Schemas**
       - Demonstrated **inheritance implementation**.
       - Example: `PosInvoice` schema **extended** the `Invoice` schema.
       - **Problem**: AVRO cannot handle this inheritance.
- **Solution**
  - **Combine** the `Invoice` schema into the `PosInvoice` schema.
  - **Eliminate** the `Invoice` schema.
  - Left with **only three schemas**.
    - These will be our **baseline schemas** for the current lecture.

---

## Creating the Solution

- **Goal**
  - Define objects using a **simple schema definition language** (AVRO).
  - Automatically generate **serializable classes**.
- **Steps**
  1. **Create a New Maven Project**
     - Set up the project environment.
  2. **Define Schemas**
     - Use AVRO schema definitions.

---

## Defining AVRO Schemas

### Setting Up Schema Definitions

- **Create a Folder**
  - Under **project resources**:
    - This is where all **schema definitions** will be stored.

### General Schema Structure

- **Syntax Overview**
  - AVRO schema definition syntax is **straightforward**.
- **Required Components**
  1. **Namespace**
     - Defines the **Java package**.
     - Example:
       ```json
       "namespace": "com.example.avro"
       ```
  2. **Type**
     - Typically set to `"record"` for class definitions.
     - Indicates the element type.
     - Example:
       ```json
       "type": "record"
       ```
  3. **Name**
     - The **name of the class**.
     - Example:
       ```json
       "name": "DeliveryAddress"
       ```
- **Fields**
  - Define a **list of fields** for the record.
  - Each field includes:
    - **Name**
    - **Type**
    - **Optional Nullability**

### Defining the First Schema (`DeliveryAddress`)

- **Example Schema**
  ```json
  {
    "namespace": "com.example.avro",
    "type": "record",
    "name": "DeliveryAddress",
    "fields": [
      {
        "name": "AddressLine",
        "type": "string"
      },
      {
        "name": "City",
        "type": "string"
      },
      {
        "name": "State",
        "type": "string"
      },
      {
        "name": "ZipCode",
        "type": "string"
      }
    ]
  }
  ```
- **Notes**
  - Each field is enclosed in `{}`.
  - **Nullability**
    - To allow `null` values, explicitly define using a **union type**:
      ```json
      "type": ["null", "string"]
      ```
    - Enabling `null` is **explicitly required** in AVRO schemas.

### Defining the `LineItem` Schema

- **Example Schema**
  ```json
  {
    "namespace": "com.example.avro",
    "type": "record",
    "name": "LineItem",
    "fields": [
      {
        "name": "ItemCode",
        "type": "string"
      },
      {
        "name": "ItemDescription",
        "type": "string"
      },
      {
        "name": "ItemPrice",
        "type": "double"
      },
      {
        "name": "ItemQty",
        "type": "int"
      },
      {
        "name": "TotalValue",
        "type": "double"
      }
    ]
  }
  ```
- **Notes**
  - Fields are defined similarly to the first schema.

### Defining the `PosInvoice` Schema

- **Start as Before**
  - Define `namespace`, `type`, and `name`.
- **Fields**
  - **Standard Fields**
    - Example fields: `InvoiceNumber`, `CreatedTime`, `StoreID`, `CustomerCardNo`, etc.
  - **Complex Fields**
    1. **`DeliveryAddress` Field**
       - **Type**: `"DeliveryAddress"` (refers to the previously defined schema).
       - **Definition**
         ```json
         {
           "name": "DeliveryAddress",
           "type": "com.example.avro.DeliveryAddress"
         }
         ```
    2. **`InvoiceLineItems` Field**
       - **Type**: An **array** of `LineItem` objects.
       - **Definition**
         ```json
         {
           "name": "InvoiceLineItems",
           "type": {
             "type": "array",
             "items": "com.example.avro.LineItem"
           }
         }
         ```
       - **Explanation**
         - The type is a **complex type** requiring its own `{}`.
         - Within braces:
           - `"type": "array"`
           - `"items": "com.example.avro.LineItem"`

### Completing the Schemas

- **Final Notes**
  - **Cross-Referencing**
    - When a field's type is another record, reference it by its **full class name**.
  - **Arrays**
    - Defined using the `"array"` type and specifying `"items"`.

---

## Generating Class Definitions

### Using AVRO Maven Plugin

- **Modify `pom.xml`**
  - **Maven Compiler Plugin**
    - Ensure JDK version is set to **1.8**.
    - Example:
      ```xml
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.1</version>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
        </configuration>
      </plugin>
      ```
  - **AVRO Maven Plugin**
    - Include the plugin with execution details.
    - **Configuration Parameters**
      - **Source Directory**: Location of schema files.
        ```xml
        <sourceDirectory>${project.basedir}/src/main/resources/schemas</sourceDirectory>
        ```
      - **Output Directory**: Where generated classes will be placed.
        ```xml
        <outputDirectory>${project.basedir}/src/main/java</outputDirectory>
        ```
      - **Imports**: Since schemas reference each other, specify imports.
        ```xml
        <imports>
          <import>${project.basedir}/src/main/resources/schemas/DeliveryAddress.avsc</import>
          <import>${project.basedir}/src/main/resources/schemas/LineItem.avsc</import>
        </imports>
        ```
  - **AVRO Dependency**
    - Include the AVRO library to compile generated code.
    - Example:
      ```xml
      <dependency>
        <groupId>org.apache.avro</groupId>
        <artifactId>avro</artifactId>
        <version>1.10.2</version>
      </dependency>
      ```

### Compiling the Project

- **Build Process**
  - Use Maven lifecycle to compile the project.
    - Run `mvn clean compile`.
- **Outcome**
  - The build generates **AVRO source code**.
  - All classes are generated.
- **Resulting Classes**
  - Generated classes are **serializable** using the **Confluent AVRO serializer**.

---

## Conclusion

- **Achievements**
  - Learned how to generate **POJOs from AVRO schemas**.
  - Addressed the **inheritance limitation** by combining schemas.
- **Next Steps**
  - Will cover how to **use the AVRO-produced POJOs in Kafka producers** in upcoming lectures.
- **Closing Remarks**
  - "See you in the next lecture."
  - "**Keep learning and keep growing.**"
  - **[Outro Music]**

---

**Note:** This mindmap covers all the information provided in the transcript, ensuring that no details are missed. It includes the steps for defining AVRO schemas, handling limitations, generating class definitions using Maven plugins, and preparing for further integration with Kafka producers.