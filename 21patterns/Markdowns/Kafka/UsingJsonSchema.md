# Using JSON Schema Mindmap

## Introduction

- **Objective**: Create schema definitions and generate POJOs (Plain Old Java Objects) from those schemas using JSON Schema.

---

## Problem Statement

- **Model an Invoice Event**:
  - **Invoice**:
    - Complex Java object containing fields:
      - `InvoiceNumber`
      - `CreatedTime`
      - `CustomerID`
      - `TotalAmount`
    - **Field Types**: `String`, `Long`, `Number`, `Integer`
  - **InvoiceLineItems**:
    - Array of `InvoiceLineItem` objects
    - **InvoiceLineItem**:
      - Fields:
        - `ItemCode`
        - `ItemDescription`
        - `ItemPrice`
        - `ItemQty`
        - `TotalValue`
      - **Field Types**: `String`, `Number`, `Integer`
  - **DeliveryAddress**:
    - Separate object with fields:
      - `AddressLine`
      - `State`
      - `PinCode`
  - **POSInvoice**:
    - Inherits from `Invoice` object
    - Includes all fields and `InvoiceLineItems` array
    - Additional fields:
      - `StoreID`
      - `CashierID`
      - `DeliveryType`
      - `DeliveryAddress`

- **Goal**:
  - Transmit `POSInvoice` objects to Kafka broker.
  - Model events as typical Java classes using Object-Oriented Programming (OOP) principles.

---

## Solution

- **Define Objects Using Schema Definition Language**:
  - Use JSON Schema to define the structure of each object.
- **Automatically Generate Serializable Classes**:
  - Utilize the open-source project **`jsonschema2pojo`** to generate Java classes from JSON Schema definitions.
  - Capable of producing both Java and Scala code.

---

## Steps

### 1. Create a New Maven Project

- **Set Up Project Structure**:
  - Create a folder under `src/main/resources` to store all JSON schema definitions.

### 2. Define Schema Definitions Using JSON Syntax

- **Common Schema Structure**:
  - **`type`**: Set to `"object"`.
  - **`javaType`**: Fully qualified name of the target Java class.
  - **`properties`**: Define each field in the class with its type.

#### a. `LineItem.json` Schema

- **Fields and Types**:
  - `itemCode`: `string`
  - `itemDescription`: `string`
  - `itemPrice`: `number`
  - `itemQty`: `integer`
  - `totalValue`: `number`
- **Example**:
  ```json
  {
    "type": "object",
    "javaType": "com.example.types.LineItem",
    "properties": {
      "itemCode": { "type": "string" },
      "itemDescription": { "type": "string" },
      "itemPrice": { "type": "number" },
      "itemQty": { "type": "integer" },
      "totalValue": { "type": "number" }
    }
  }
  ```

#### b. `DeliveryAddress.json` Schema

- **Fields and Types**:
  - `addressLine`: `string`
  - `city`: `string`
  - `state`: `string`
  - `pinCode`: `string`
- **Example**:
  ```json
  {
    "type": "object",
    "javaType": "com.example.types.DeliveryAddress",
    "properties": {
      "addressLine": { "type": "string" },
      "city": { "type": "string" },
      "state": { "type": "string" },
      "pinCode": { "type": "string" }
    }
  }
  ```

#### c. `Invoice.json` Schema

- **Fields and Types**:
  - `invoiceNumber`: `string`
  - `createdTime`: `long` (using `javaType`)
  - `customerId`: `string`
  - `totalAmount`: `number`
  - `numberOfItems`: `integer`
  - `paymentMethod`: `string`
  - `invoiceLineItems`: `array` of `LineItem`
- **Handling `long` Type**:
  - Use `"javaType": "java.lang.Long"` for `createdTime`.
- **Example**:
  ```json
  {
    "type": "object",
    "javaType": "com.example.types.Invoice",
    "properties": {
      "invoiceNumber": { "type": "string" },
      "createdTime": { "javaType": "java.lang.Long" },
      "customerId": { "type": "string" },
      "totalAmount": { "type": "number" },
      "numberOfItems": { "type": "integer" },
      "paymentMethod": { "type": "string" },
      "invoiceLineItems": {
        "type": "array",
        "items": { "$ref": "LineItem.json" }
      }
    }
  }
  ```

#### d. `POSInvoice.json` Schema

- **Inheritance**:
  - Extends `Invoice` using `"extends"` property.
- **Additional Fields**:
  - `storeId`: `string`
  - `cashierId`: `string`
  - `deliveryType`: `string`
  - `deliveryAddress`: Reference to `DeliveryAddress`
- **Example**:
  ```json
  {
    "type": "object",
    "javaType": "com.example.types.POSInvoice",
    "extends": { "$ref": "Invoice.json" },
    "properties": {
      "storeId": { "type": "string" },
      "cashierId": { "type": "string" },
      "deliveryType": { "type": "string" },
      "deliveryAddress": { "$ref": "DeliveryAddress.json" }
    }
  }
  ```

### 3. Configure `jsonschema2pojo` Maven Plugin

- **Add Plugin to `pom.xml`**:
  ```xml
  <build>
    <plugins>
      <plugin>
        <groupId>org.jsonschema2pojo</groupId>
        <artifactId>jsonschema2pojo-maven-plugin</artifactId>
        <version>1.0.2</version>
        <executions>
          <execution>
            <goals>
              <goal>generate</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <sourceDirectory>${project.basedir}/src/main/resources/</sourceDirectory>
          <targetPackage>com.example.types</targetPackage>
          <outputDirectory>${project.build.directory}/generated-sources/</outputDirectory>
        </configuration>
      </plugin>
    </plugins>
  </build>
  ```
- **Plugin Configuration Details**:
  - **`sourceDirectory`**: Directory containing JSON schemas.
  - **`targetPackage`**: Base package for generated classes.
  - **`outputDirectory`**: Where generated classes will be placed.

### 4. Add Required Dependencies

- **Jackson Databind**:
  ```xml
  <dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.13.3</version>
  </dependency>
  ```
- **Apache Commons Lang**:
  ```xml
  <dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.12.0</version>
  </dependency>
  ```
- **Maven Compiler Plugin** (Set Java Version to 1.8):
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

### 5. Generate Classes

- **Compile the Project**:
  - Use Maven lifecycle to run the `compile` phase.
  - Command: `mvn compile`
- **Result**:
  - Generated Java classes will appear in the specified `outputDirectory`.
  - Classes include Jackson annotations for JSON serialization/deserialization.

---

## Conclusion

- **Outcome**:
  - Successfully generated POJO classes from JSON Schema definitions using `jsonschema2pojo`.
  - Classes are ready to be serialized and sent to Kafka.
- **Next Steps**:
  - Implement serialization and deserialization using JSON.
  - Continue learning about Avro schemas in the upcoming lectures.

---

**Note**: This mindmap captures all the steps and details from defining the problem statement to generating the Java classes using JSON Schema and `jsonschema2pojo`. Each step includes essential information to ensure a comprehensive understanding of the process.