# Kafka IDE Setup for Examples Mindmap

## Overview

- **Introduction**
  - The lecture explains step-by-step how to set up the same environment used in the course demos.
  - Using **IntelliJ IDEA** as the development IDE.
  - The course uses **Confluent Kafka Community Edition**.
- **Purpose**
  - To set up the IDE and environment to run the Kafka examples provided in the course.
  - Adjust configurations to make local development more convenient.

## Adjusting Kafka Configurations for Local Development

- **Issue with Default Configuration**
  - The earlier configuration creates log files in the **temp** directory.
  - Using the same Kafka cluster installation for all examples is sometimes not convenient.
- **Solution: Use Separate Data Directory per Example**
  - Change the data log directory to the current directory.
  - Every time you start the Kafka cluster from your IDE, it will create new logs in the current directory.
  - This approach works like running a separate Kafka cluster for each example.

## Modifying Configuration Files

- **Editing `zookeeper.properties`**
  - Open the `zookeeper.properties` file.
  - Place a double dot (`..`) at the beginning of the data directory configuration line.
    - This changes the data directory to the current directory.
  - Save the file.
- **Editing `server.properties`**
  - Do the same modification for the `server.properties` file.
  - Repeat for all three configuration files (since there are three brokers).
- **Result**
  - Kafka and Zookeeper will now use the current directory for data logs.
  - Each example will have its own data directory, keeping data isolated per project.

## Setting Up Environment Variable

- **Setting `KAFKA_HOME` Environment Variable**
  - To avoid typing absolute paths when running scripts.
- **On Windows**
  - Use the command:
    ```batch
    set KAFKA_HOME=C:\path\to\kafka
    ```
- **On Linux or Mac**
  - Use the appropriate command for your operating system:
    ```bash
    export KAFKA_HOME=/path/to/kafka
    ```

## Setting Up IntelliJ IDEA

- **Assumptions**
  - You already have IntelliJ IDEA installed.
  - You know how to install it and create Java projects using IntelliJ.
- **Downloading Example Projects**
  - Download the example projects from the lecture resources.
  - Uncompress the downloaded file.
  - You should see a directory structure similar to the one shown in the lecture.
- **Opening the Example Project**
  - Start IntelliJ IDEA.
  - Open the example project by selecting the project directory.

## Using Scripts in the Examples

- **Included Scripts**
  - All examples include scripts to start Kafka services, create topics, and perform other necessary tasks.
  - The current example has several scripts.
- **Script Details**
  - All scripts are **Windows batch files** (`.bat`).
- **Example Script to Start Zookeeper**
  - The script uses the `KAFKA_HOME` environment variable.
  - Navigates to `bin\windows` and starts the batch file to run Zookeeper:
    ```batch
    %KAFKA_HOME%\bin\windows\zookeeper-server-start.bat %KAFKA_HOME%\config\zookeeper.properties
    ```
  - Specifies the Zookeeper properties file location using the environment variable.

## Adjusting Scripts for Linux or Mac

- **Modifications Needed**
  - If using Linux or Mac, you need to modify the scripts.
- **Changes to Make**
  - Use `$KAFKA_HOME` instead of `%KAFKA_HOME%`.
  - Change backslashes (`\`) to forward slashes (`/`).
  - Remove the `.bat` extension from script names.
- **Example Modified Script**
  - For starting Zookeeper on Linux/Mac:
    ```bash
    $KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties
    ```
- **Permissions**
  - Ensure that the shell scripts have execute permissions:
    ```bash
    chmod +x script-name.sh
    ```
- **General Note**
  - These are simple changes, and you should already be familiar with making them.

## Running Kafka Services from IntelliJ IDEA

- **Starting Zookeeper and Kafka Brokers**
  - You can start Zookeeper server from the IDE itself.
  - The output will appear in a docked window inside the IDE.
- **Batch Script Support Plugin**
  - If you do not see the run menu option in IntelliJ for batch scripts, you might need to install a **Batch Script Support** plugin.
  - **Installing the Plugin**
    - Go to `File` > `Settings` > `Plugins` in IntelliJ.
    - Search for "Batch Scripts Support" and install it.
- **Starting Kafka Brokers**
  - Start the first Kafka broker using the provided script.
  - Repeat for the second and third brokers.

## Creating a Topic

- **Create a Topic**
  - Use the provided script to create a topic in Kafka.
- **Observing the Data Directory**
  - After starting services and creating a topic, a `tmp` directory is created in the project's current directory.
  - This `tmp` directory is the home for Kafka and Zookeeper data.
  - All data for this project is stored here.

## Running Examples and Isolating Data

- **Running the Example**
  - Now you can run your example, send data, process it, and perform other operations.
- **Data Isolation**
  - All data for this project remains in the current directory of the project.
  - When starting another project, its data and log files remain isolated in its own directory.
- **Cleaning Up**
  - When done with a project or to start fresh:
    - Stop all services (Zookeeper and Kafka brokers).
    - Delete the `tmp` directory to remove all data.
  - This makes cleanup simple and straightforward.

## Benefits of This Approach

- **Convenience in Development**
  - Makes local development more convenient and manageable.
- **Data Isolation**
  - Keeps data and log files isolated per project.
  - Prevents conflicts and confusion between different examples.
- **Simplified Cleanup**
  - Easy to clean up data and restart projects.
- **Enhanced Development Experience**
  - Allows you to focus on development without worrying about managing shared data directories.

## Conclusion

- **Summary**
  - Explained how to set up the IDE and environment to match the course demos.
  - Showed how to modify configurations and scripts to use separate data directories per example.
  - Demonstrated starting Kafka services from within IntelliJ IDEA.
- **Encouragement**
  - Keep learning and keep growing.

---

