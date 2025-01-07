Certainly! Based on the screenshots, here's a detailed explanation of the **purpose of each table**, its **columns and their roles**, and the **connections with other tables**. I'll consolidate all the available information to make it clear and structured.

---

## **1. `user_details`**
### **Purpose**:
- Stores user-related information, including their role assignments.

### **Columns**:
- `id`: Primary key, unique identifier for a user.
- `v_user_code`: Unique user code.
- `v_name`: Name of the user.
- `v_email`: Email of the user.
- `v_role_code`: Foreign key referencing `role_details` to assign a role to the user.

### **Connections**:
- **One-to-Many**: A role in `role_details` can be assigned to multiple users in `user_details`.

---

## **2. `role_details`**
### **Purpose**:
- Maintains role definitions and metadata.

### **Columns**:
- `id`: Primary key, unique identifier for a role.
- `v_role_code`: Unique role code (Primary Key).
- `v_role_name`: Name of the role.
- `v_role_description`: Description of the role.
- `v_role_status`: Status of the role (e.g., Active/Inactive).

### **Connections**:
- **One-to-Many**: Links to `user_details` using `v_role_code`.

---

## **3. `data_contracts`**
### **Purpose**:
- Central table managing metadata for data contracts between systems.

### **Columns**:
- `id`: Primary key.
- `v_contract_code`: Unique identifier for the data contract.
- `v_contract_name`: Descriptive name of the contract.
- `v_source_system` and `v_target_system`: Foreign keys referencing `data_system`, linking the source and target systems.
- `v_source_owner_code` and `v_ingestion_owner_code`: Links to owners of the source and ingestion processes.
- `v_frequency`: Frequency of data ingestion (foreign key to `data_frequency`).
- `v_source_connection_type`: Type of connection used for the source (foreign key to `connection_details`).
- `v_data_contract_status`: Current status of the contract (foreign key to `data_contract_statuses`).
- Metadata: Includes `created_by`, `updated_by`, `effective_date`, and `expiration_date`.

### **Connections**:
- **One-to-Many**:
  - Links to `data_system` for source and target systems.
  - Links to `data_contract_statuses` for contract status tracking.
  - Links to `data_frequency` for ingestion frequency.
- **Many-to-One**:
  - `v_source_owner_code` and `v_ingestion_owner_code` link to owners in `user_details`.

---

## **4. `data_frequency`**
### **Purpose**:
- Defines standard frequencies for data ingestion.

### **Columns**:
- `id`: Primary key.
- `v_frequency`: Frequency value (e.g., Daily, Weekly).

### **Connections**:
- **One-to-Many**: Referenced by `data_contracts` to standardize ingestion intervals.

---

## **5. `data_contract_statuses`**
### **Purpose**:
- Manages contract statuses and their descriptions.

### **Columns**:
- `id`: Primary key.
- `v_data_contract_status`: Status of the contract (e.g., Active, Inactive).
- `v_data_contract_status_description`: Description of the status.

### **Connections**:
- **One-to-Many**: Referenced by `data_contracts` to track contract status.

---

## **6. `data_hierarchy_contracts`**
### **Purpose**:
- Tracks dependencies between data contracts.

### **Columns**:
- `id`: Primary key.
- `v_contract_code`: Foreign key referencing `data_contracts`.
- `depends_on`: References another contract that the current one depends on.
- `v_data_contract_status`: Foreign key referencing the status of the contract.

### **Connections**:
- **Self-Referencing**: Tracks dependencies between contracts in `data_contracts`.

---

## **7. `data_system`**
### **Purpose**:
- Maintains the metadata of systems involved in data contracts.

### **Columns**:
- `id`: Primary key.
- `v_system_name`: Name of the system.
- `v_connection_id`: Foreign key referencing `connection_details`.

### **Connections**:
- **One-to-Many**: Referenced by `data_contracts` for source and target systems.

---

## **8. `connection_details`**
### **Purpose**:
- Stores details about the connections used for data contracts.

### **Columns**:
- `id`: Primary key.
- `v_connection_id`: Unique identifier for a connection.
- `v_connection_type`: Type of connection (e.g., JDBC, API, etc.).

### **Connections**:
- **One-to-Many**: Referenced by `data_system` and `data_contracts`.

---

## **9. `businessline_datacontract_link`**
### **Purpose**:
- Maps business lines to data contracts.

### **Columns**:
- `id`: Primary key.
- `v_business_line_code`: Foreign key referencing `business_line_details`.
- `v_contract_code`: Foreign key referencing `data_contracts`.
- `v_data_contract_status`: Tracks the status of the contract.

### **Connections**:
- **Many-to-One**:
  - Links to `business_line_details` using `v_business_line_code`.
  - Links to `data_contracts` using `v_contract_code`.

---

## **10. `business_line_details`**
### **Purpose**:
- Stores metadata for business lines.

### **Columns**:
- `id`: Primary key.
- `v_business_line_code`: Unique identifier for the business line.
- `v_business_line_name`: Name of the business line.
- `v_business_line_description`: Description of the business line.

### **Connections**:
- **One-to-Many**: Referenced by `businessline_datacontract_link`.

---

### **Table Connections Overview**:
- `data_contracts` is the central table connecting `data_system`, `data_contract_statuses`, `data_frequency`, and `user_details` through foreign keys.
- `data_hierarchy_contracts` introduces self-referencing relationships for contract dependencies.
- `businessline_datacontract_link` and `business_line_details` connect data contracts to business lines.

This model is robust, supporting:
- Contract metadata management.
- System and connection tracking.
- Business line associations.
- Contract dependency and lineage.

If you'd like further details on any table or concept, feel free to ask!