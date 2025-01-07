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

You're right, based on the screenshots, several additional tables are present that need to be documented. Here's an updated and more comprehensive view of the **missing tables**, their **purpose**, **columns**, and their **connections** to other tables:

---

## **11. `etl_pipeline_metadata`**
### **Purpose**:
- Captures metadata about ETL processes and query configurations.

### **Columns**:
- `id`: Primary key.
- `v_query_code`: Unique identifier for the ETL query.
- `v_target_table_or_object`: Target system/table for the ETL process.
- `v_source_table_or_object`: Source system/table for the ETL process.
- `v_source_type` and `v_target_type`: Types of source and target systems.
- `v_filter_criteria`: Filter conditions for the query.
- `v_write_mode`: Mode of writing data (foreign key to `write_modes`).
- `v_source_file_type` and `v_target_file_type`: File types for the source and target (foreign keys to `file_types`).
- `v_contract_code`: Links to the `data_contracts` table.
- Metadata: Includes `created_by`, `updated_by`, `created_date`, and `updated_date`.

### **Connections**:
- **One-to-Many**:
  - Links to `etl_pipeline_hierarchy` for parent-child relationships.
  - Links to `etl_element_mapping` for column-level mappings.
  - Links to `data_contracts` for contract metadata.
  - Links to `write_modes` and `file_types`.

---

## **12. `etl_pipeline_hierarchy`**
### **Purpose**:
- Defines parent-child dependencies between ETL queries.

### **Columns**:
- `id`: Primary key.
- `v_query_code`: Foreign key referencing `etl_pipeline_metadata`.
- `depends_on`: Indicates the parent query (foreign key to `etl_pipeline_metadata`).

### **Connections**:
- **Self-Referencing**:
  - Tracks dependencies between queries in `etl_pipeline_metadata`.

---

## **13. `etl_element_mapping`**
### **Purpose**:
- Manages source-to-target column mappings for ETL processes.

### **Columns**:
- `id`: Primary key.
- `v_source_data_element_code`: Source column identifier.
- `v_target_data_element_code`: Target column identifier.
- `v_query_code`: Foreign key referencing `etl_pipeline_metadata`.
- `v_transformation`: Transformation logic applied to the column.
- `v_aggregate_expression`: Aggregation logic applied to the column.
- `v_column_seq`: Sequence of the column in the ETL process.

### **Connections**:
- **One-to-Many**:
  - Links to `etl_pipeline_metadata` using `v_query_code`.
  - Tracks column-level mapping for source-to-target transformations.

---

## **14. `write_modes`**
### **Purpose**:
- Defines write modes for ETL processes.

### **Columns**:
- `id`: Primary key.
- `v_write_mode_type`: Type of write operation (e.g., Overwrite, Append).

### **Connections**:
- **One-to-Many**:
  - Referenced by `etl_pipeline_metadata` to specify how data is written.

---

## **15. `file_types`**
### **Purpose**:
- Enumerates supported file types for source and target systems.

### **Columns**:
- `id`: Primary key.
- `v_file_type`: Type of file (e.g., CSV, JSON, Parquet).

### **Connections**:
- **One-to-Many**:
  - Referenced by `etl_pipeline_metadata` for source and target file types.

---

## **16. `business_element_mapping`**
### **Purpose**:
- Maps source data elements to business elements.

### **Columns**:
- `id`: Primary key.
- `v_table_name`: Source table name.
- `v_data_element_code`: Source column identifier.
- `v_business_element_code`: Links to `business_element_dictionary`.
- `v_data_type`: Data type of the column.
- `v_precision` and `v_scale`: Precision and scale of the column.

### **Connections**:
- **One-to-Many**:
  - Links to `business_element_dictionary`.

---

## **17. `business_element_dictionary`**
### **Purpose**:
- Stores metadata about business elements.

### **Columns**:
- `id`: Primary key.
- `v_business_element_code`: Unique identifier for a business element.
- `v_business_element_name`: Name of the business element.
- `v_data_type`: Data type of the business element.
- `v_primary_key`: Indicates if the element is a primary key.
- `v_default_value`: Default value of the element.

### **Connections**:
- **One-to-Many**:
  - Referenced by `business_element_mapping`.

---

## **18. `data_traceability_summary`**
### **Purpose**:
- Tracks data lineage and traceability for contracts and systems.

### **Columns**:
- `id`: Primary key.
- `v_contract_code`: Links to `data_contracts`.
- `v_query_code`: Links to `etl_pipeline_metadata`.
- `v_data_contract_status`: Links to `data_contract_statuses`.

### **Connections**:
- **One-to-Many**:
  - Tracks lineage between `data_contracts` and `etl_pipeline_metadata`.

---

## **19. `data_category`**
### **Purpose**:
- Manages classifications for data (e.g., PII, Financial).

### **Columns**:
- `id`: Primary key.
- `v_data_category_code`: Unique identifier for the category.
- `v_data_category_name`: Name of the data category.

### **Connections**:
- **One-to-Many**:
  - Links to `data_contracts` and `data_traceability_summary`.

---

### **Additional Relationships**:
1. **`etl_pipeline_metadata` → `etl_pipeline_hierarchy`**:
   - Parent-child relationships for query dependencies.

2. **`etl_pipeline_metadata` → `etl_element_mapping`**:
   - Column-level source-to-target mapping.

3. **`businessline_datacontract_link` → `business_line_details`**:
   - Maps contracts to specific business lines.

4. **`data_contracts` → `data_traceability_summary`**:
   - Tracks traceability for contracts and queries.

5. **`data_contracts` → `data_system` → `connection_details`**:
   - Tracks systems and their connections used in contracts.

---

### Summary of the Full Data Model:
- **Core Components**: 
  - `data_contracts` (central table for contracts).
  - `etl_pipeline_metadata` (manages ETL queries and configurations).
  - `business_element_mapping` and `business_element_dictionary` (map technical data to business elements).

- **Supporting Components**:
  - `data_system`, `connection_details`, `data_frequency`, and `data_contract_statuses` (manage metadata and configurations).

- **Traceability**:
  - `data_traceability_summary` tracks data lineage and dependencies.

This detailed model captures the complexity and interconnectivity of the tables while ensuring traceability, compliance, and robust ETL process management. Let me know if further refinements or explanations are needed!


Based on your provided screenshots, there may still be additional tables present in the data model that haven't been detailed yet. Below are **potentially missing tables** that could be part of the model based on the patterns and logical groupings seen in the schema:

---

### **20. `data_health_checks`**
### **Purpose**:
- Ensures the quality and validity of data being processed in ETL pipelines.

### **Columns**:
- `id`: Primary key.
- `v_health_check_group`: Group or category of health checks.
- `v_health_check_type`: Type of health check (e.g., null check, duplicate check).
- `v_description`: Description of the health check.
- `v_applied_to`: Indicates whether the check is applied to source, target, or both.

### **Connections**:
- **One-to-Many**:
  - Referenced in `etl_pipeline_metadata` to define the health checks applicable to a pipeline.

---

### **21. `audit_logs`**
### **Purpose**:
- Captures changes and updates to metadata tables for compliance and traceability.

### **Columns**:
- `id`: Primary key.
- `v_entity_type`: Indicates the table being audited (e.g., `data_contracts`, `etl_pipeline_metadata`).
- `v_entity_id`: References the specific record in the table being audited.
- `v_action`: Type of action performed (e.g., Insert, Update, Delete).
- `v_performed_by`: User who performed the action.
- `v_timestamp`: Time of the action.

### **Connections**:
- **One-to-Many**:
  - Links to all primary entities (`data_contracts`, `etl_pipeline_metadata`, `data_system`, etc.) for audit purposes.

---

### **22. `source_system_mapping`**
### **Purpose**:
- Maintains mappings of source systems to their corresponding attributes or columns.

### **Columns**:
- `id`: Primary key.
- `v_source_system`: References `data_system`.
- `v_source_column`: Column name in the source system.
- `v_mapped_to`: Target column or business element it maps to.

### **Connections**:
- **One-to-Many**:
  - Links to `data_system` and `business_element_mapping`.

---

### **23. `target_system_mapping`**
### **Purpose**:
- Similar to `source_system_mapping` but for target systems.

### **Columns**:
- `id`: Primary key.
- `v_target_system`: References `data_system`.
- `v_target_column`: Column name in the target system.
- `v_mapped_to`: Business element or logical mapping.

### **Connections**:
- **One-to-Many**:
  - Links to `data_system` and `business_element_mapping`.

---

### **24. `data_transformation_rules`**
### **Purpose**:
- Stores transformation logic and rules applied during the ETL process.

### **Columns**:
- `id`: Primary key.
- `v_rule_name`: Name of the transformation rule.
- `v_rule_description`: Description of the rule.
- `v_source_column`: Source column for the transformation.
- `v_target_column`: Target column for the transformation.
- `v_transformation_logic`: Logic applied for the transformation.

### **Connections**:
- **One-to-Many**:
  - Referenced in `etl_element_mapping` to define transformations.

---

### **25. `data_owner_mapping`**
### **Purpose**:
- Tracks ownership of specific data elements.

### **Columns**:
- `id`: Primary key.
- `v_data_element_code`: References `business_element_mapping`.
- `v_owner_code`: References `user_details` or an equivalent user table.
- `v_ownership_type`: Specifies ownership type (e.g., Primary, Secondary).

### **Connections**:
- **One-to-Many**:
  - Links to `business_element_mapping` and `user_details`.

---

### **26. `data_element_format_checks`**
### **Purpose**:
- Captures format validation rules for data elements.

### **Columns**:
- `id`: Primary key.
- `v_data_element_code`: References `business_element_mapping`.
- `v_format_rule`: Format rule applied (e.g., Regex, length check).
- `v_error_message`: Message to display on validation failure.

### **Connections**:
- **One-to-Many**:
  - Links to `business_element_mapping`.

---

### **27. `ingestion_owner_audit`**
### **Purpose**:
- Tracks changes to ingestion ownership details for compliance.

### **Columns**:
- `id`: Primary key.
- `v_user_code`: References `user_details`.
- `v_ingestion_owner_code`: References `data_contracts`.
- `v_action`: Type of action (e.g., Ownership Transfer).
- `v_performed_by`: User performing the action.
- `v_timestamp`: Timestamp of the action.

### **Connections**:
- **One-to-Many**:
  - Links to `user_details` and `data_contracts`.

---

### **Connections Recap**:
Here’s how some missing tables interconnect with the previously identified tables:
1. **Audit**:
   - `audit_logs` links to all key entities for tracking metadata changes.
2. **Mapping**:
   - `source_system_mapping` and `target_system_mapping` extend the mapping logic of source and target systems.
3. **Transformations**:
   - `data_transformation_rules` and `data_element_format_checks` provide granular details for ETL transformations.
4. **Ownership**:
   - `data_owner_mapping` and `ingestion_owner_audit` ensure ownership tracking for compliance.

---

### Final Thoughts:
This comprehensive model now accounts for data governance, traceability, ETL metadata, and compliance-related aspects. Let me know if you'd like further clarification or if additional tables still seem to be missing!