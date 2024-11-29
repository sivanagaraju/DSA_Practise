# Summing up the Producers: POS Simulator using AVRO Serialized Invoices Mindmap

## Introduction

- **Recap**
  - In the earlier video, we learned to **auto-generate AVRO serializable POJOs** from the schema definition.
- **Objective**
  - In this lecture, we are going to **use them in a Kafka Producer program**.

---

## Using the POS Simulator with AVRO

- **POS Simulator Program**
  - Created in an **earlier lecture**.
  - Previously sent **realistic invoices** to Kafka.
  - Messages were serialized using **JSON serializer**.
- **Plan**
  - **Take the same example**.
  - **Copy the code**.
  - Make **necessary changes**.
  - Start sending **AVRO invoices**.

---

## Setting up the Project

- **AVRO Serializer**
  - Offered by the **Confluent Platform**.
- **Development Environment**
  - Develop and execute this example on **Confluent Community Edition**.

---

## Creating a New Maven Project

- **Step-by-Step Process**
  - Create a **brand new Maven project** from scratch.
  - Show the process so you can **do it yourself**.

---

## Setting up Maven Dependencies

- **Use JDK 1.8**
  - Like all other projects.
  - Define a **property** for the JDK version.
- **Define Confluent Version**
  - Using **Confluent 5.3.0**.
  - Define a **property** for the Confluent version.
- **Kafka Version**
  - Use **Kafka version** that comes with Confluent 5.3.0.
  - Necessary to **avoid version conflicts**.
  - Confluent defines Kafka version in their platform.
- **Custom Maven Repository**
  - Confluent artifacts are **not hosted in standard Maven repository**.
  - Need to **add a custom repository** in the `pom.xml`.
- **Define Dependencies**
  - **Kafka AVRO Serializer**
    - Offered by **Confluent**.
    - Previously used JSON serializer; now use **AVRO serializer** created by Confluent.
  - **Kafka Client Libraries**
    - Required to **create a producer**.
  - **Log4j Dependency**
    - For **logging purposes**.
- **Adding to `pom.xml`**
  - **Properties and Repositories**
    - Add properties for versions.
    - Add the custom repository for Confluent packages.
  - **Dependencies**
    - Include necessary dependencies in the `pom.xml`.

---

## Copying Schema Definitions

- **Open Previous Project**
  - The project that **generated Java classes from AVRO schema**.
- **Copy Schema Definitions**
  - Copy the **AVRO schema definitions** into the new project's resources.

---

## Including AVRO Maven Plugin

- **Copy AVRO Maven Plugin**
  - From the **previous project**.
- **Paste into `pom.xml`**
  - Include the plugin execution details in the new project's `pom.xml`.

---

## Adding Log4j Configuration

- **Copy Log4j Configuration File**
  - From another **earlier project**.
- **Paste into the Project**
  - Place the `log4j2.xml` file in the appropriate directory.

---

## Compiling the Project

- **Ready to Compile**
  - After setting up **schema definitions** and **Maven dependencies**.
- **Compile the Project**
  - Run Maven **compile** to generate Java classes from AVRO schemas.
- **Handling Warnings**
  - If warnings appear, **add a line in `pom.xml` properties** to fix them.
  - Recompile the project.

---

## Recap of Progress

- **Steps Completed**
  - Created an **empty Maven project**.
  - Defined **dependencies** to work with the Confluent platform.
  - Copied **AVRO schema definitions** from the earlier project.
- **Summary**
  - Essentially replicated the **AVRO to POJO project** with additional dependencies.
  - Project is essentially the **same as the AVRO to POJO example**.

---

## Modifying the POS Simulator

- **Goal**
  - Make the POS Simulator **send AVRO** instead of JSON.
- **Approach**
  - Open the **old POS Simulator** project.
  - **Copy most of the code**.
  - Make only **necessary changes**.

---

## Copying Data Generator and Sample Data Directory

- **Components Needed**
  - **Types** (Java classes generated from AVRO schemas).
  - **Data Generator** package.
  - **Sample Data** directory.
- **Copy to Current Project**
  - Transfer these components to the new project.

---

## Fixing Errors

- **InvoiceGenerator Class Error**
  - Error: **"String cannot be applied to CharSequence."**
- **Cause**
  - AVRO Maven plugin uses **`CharSequence`** instead of **`String`**.
- **Solution**
  - Convert **`CharSequence` to `String`** in the code.

---

## Removing JSON Serializer

- **Not Needed Anymore**
  - Remove the **`JSONSerializer`** class from the project.
- **Using AVROSerializer Instead**
  - Will use **`KafkaAvroSerializer`** provided by Confluent.

---

## Copying Additional Classes

- **Copy Three Classes**
  - Copy necessary classes related to the producer.
  - (Specific classes not detailed in the transcript.)

---

## Fixing RunnableProducer Errors

- **Error**
  - **Cannot infer arguments**.
- **Cause**
  - **`getStoreID`** is returning a **`CharSequence`**.
- **Solution**
  - Convert **`getStoreID`** to return a **`String`**.

---

## Modifying PosSimulator Class

- **Main Class**
  - `PosSimulator` is the main class where **fundamental changes** are needed.
- **Previous Steps**
  - Assembled components and fixed simple errors.
- **Now**
  - Need to make **fundamental changes** to make it work with AVRO.

---

## Changing Serializer

- **From `JsonSerializer` to `KafkaAvroSerializer`**
  - Replace the JSON serializer with the **AVRO serializer** in the code.

---

## Configuring Schema Registry

- **Requirement**
  - **Confluent AVROSerializer requires the Confluent Schema Registry**.
- **Add Configuration**
  - Add a configuration line for the **schema registry** in the producer properties.
  - Example:
    ```java
    properties.put("schema.registry.url", "http://localhost:8081");
    ```
- **Handling Errors**
  - If errors appear, adjust the code accordingly.
- **Moving Constants**
  - Move constants to the **`AppConfigs`** class for better organization.

---

## Final Checks

- **Review**
  - Ensure all **necessary changes** are made.
- **Project Appears Ready**
  - The project seems ready for testing.

---

## Summary of Differences Between JSON and AVRO Projects

- **Four Main Changes Needed**
  1. **Schema Definition**
     - Use **AVRO schema definitions** and **AVRO compatible types**.
  2. **Kafka AVRO Serializer**
     - Use the **`KafkaAvroSerializer`** provided by Confluent.
  3. **Schema Registry Configuration**
     - Configure the **schema registry** in producer properties.
  4. **Confluent Specific Dependencies**
     - Include **Confluent dependencies** in `pom.xml`.

---

## Testing the Project

- **Need Scripts**
  - Scripts to start services, create topics, and run the simulator.
- **Copy Scripts**
  - From the **older project**.

---

## Adjusting Scripts

- **Execution Paths**
  - Scripts need to execute from the **Confluent home directory**.
- **Modify Scripts**
  - Prefix the **Confluent home directory location** in all scripts.
- **Configuration Files**
  - Change **configuration file locations** in the scripts if necessary.

---

## Starting Schema Registry

- **Add Script**
  - Create a script to **start the schema registry** service.
- **Example Command**
  - `confluent local services schema-registry start`

---

## Starting Services

- **Start ZooKeeper and Kafka Brokers**
  - Use the adjusted scripts to start **ZooKeeper** and **Kafka brokers**.

---

## Creating the Topic and Running the Simulator

- **Define Command-Line Arguments**
  - **Topic Name**
  - **Number of Producer Threads**
  - **Milliseconds Between Messages**
- **Run the POS Simulator**
  - Execute the application with the defined arguments.

---

## Verifying Messages

- **Simulator is Sending Messages**
  - Messages are being sent to Kafka.
- **Starting a Consumer**
  - Start a Kafka consumer to see the messages.
- **Note**
  - **AVRO is a binary format**.
  - Messages are **not human-readable** in the console without deserialization.

---

## Conclusion

- **Project Files**
  - The project file is **included in your resources**.
- **Recommendation**
  - **Try it yourself**.
  - Refer to the **source code** when you get stuck.
- **Closing Remarks**
  - "Great, we are done."
  - "But I recommend you try it yourself and refer to the source code when you get stuck."
