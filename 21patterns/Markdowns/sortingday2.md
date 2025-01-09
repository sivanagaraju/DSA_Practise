Below is a **combined, comprehensive summary** that merges all the details from the previous summaries **and** integrates additional specifics about the Swagger endpoints, log file locations, and PowerShell script examples that were shown in the images. 

---

## 1. **Project Background and Timeline**
- This project began about **8 months ago** to address a critical need:  
  - Automate the **QRM (Quantitative Risk Manager)** process used for **balance sheet forecasting** (over a 42‑month horizon).  
  - Eliminate or reduce **manual steps** (previously done with Excel and VB scripts).  
- Originally, the official QRM team had **bandwidth constraints**, so another group created a **Python “wrapper”** application to handle QRM programmatic access.

---

## 2. **Purpose of the QRM Wrapper**
- **QRM** is a **vendor tool** for enterprise forecasting (rates, liquidity, risk, etc.). It is restricted by various **firewall** and **licensing** rules:
  1. It can only be accessed from within North America.  
  2. It must be accessed from approved on‑prem Windows servers.  
- **No official QRM API**: QRM uses **DLLs** (and previously VB scripts).  
- Hence, a **Python/Flask** service was created to:
  1. **Dynamically generate PowerShell scripts** at runtime.  
  2. **Call QRM DLLs** behind the scenes to export/import data or to run forecasts.  
- This wrapper is **deployed as a Windows service** on a specific on‑prem server (the “**Quad** server”), which already hosts other related applications and has the necessary firewall openings, certificates, and service accounts to talk to QRM.

---

## 3. **High-Level Architecture**

1. **Flask REST API**  
   - Runs in Python on the Quad server.  
   - Provides Swagger‑documented endpoints (listed in Section 6 below).  
   - Does **not** currently enforce integrated authentication (open endpoints within the network).  

2. **Dynamically Generated PowerShell**  
   - When the API is called, it spawns a PowerShell script with placeholders like `<DB_NAME>`, `<MARKET_NAME>`, `<ASSUMPTION_SET>`, `<STRATEGY_NAME>`, etc.  
   - These placeholders are replaced at runtime with request‑specific values (e.g. from a JSON body).  
   - The PowerShell script then **logs into QRM** (via DLL calls), selects the correct market, assumption sets, etc., and **executes** the required tasks (export, import, forecast, etc.).  
   
3. **QRM**  
   - A licensed tool that loads data, scenario definitions, and assumption sets; runs the forecasting engine; and stores results.  
   - Because QRM must be accessed from an approved server in NA, the wrapper **cannot** run in a typical cloud environment (PCF or otherwise).

---

## 4. **Deployment and Environment Details**

- **On-Prem Windows Server** (“Quad server” at `cdpwd02a9909`…)  
  - **Manual Deployment**:  
    1. Code is kept in GitHub.  
    2. A zip of the code is copied to a designated directory on the server for Dev/UAT/Prod.  
    3. A Windows service is **stopped** and **restarted** to apply changes.  
  - **Same Certificates and Service Accounts** are reused from the existing “Quad” setup (e.g., `cfdsvc…` accounts).  
- **Logging**:
  - The **logs** reside in a folder like:  
    ```
    <...>\projects\quad\Testing-QRM-Deployment\logs\
    ```
  - Files often follow a naming convention such as `app_YYYY-MM-DD.log`.  
  - This is where standard output and debug info from the Python/Flask app is appended for each run.  
- **Access Constraints**:
  - Typically, **only North America–based** team members or L2/L3 support (with “break‑glass” credentials) can RDP into the Quad server.  
  - India-based team members often rely on logs placed in shared folders or must coordinate with NA colleagues for interactive troubleshooting.

---

## 5. **Core Use Cases & Orchestration**

1. **Export** data from QRM (e.g., a planning strategy or template) so that it can be loaded into FAST (another application for user inputs/scenario data).  
2. **Import** updated data **back** into QRM after business users have made changes in FAST.  
3. **Run** QRM forecasts or “saved workflows” so QRM can compute the next 42 months of projections (interest rates, liquidity, etc.).  
4. **Get** real-time progress status on QRM runs (if supported by the wrapper).

### Integration with FAST
- The bank uses **FAST** to let end users modify scenario inputs.  
- The orchestrator triggers:
  1. QRM **Export** → data goes to FAST.  
  2. Users update data in FAST.  
  3. FAST **Export** → data returns to QRM.  
  4. QRM is run again for updated forecasts.  
- The QRM wrapper is the “middle-man” for all interactions that require direct QRM calls.

---

## 6. **Swagger Endpoints**

From the screenshots and discussion, the wrapper provides these **Swagger-documented** endpoints (there may be more, but these were shown explicitly):

1. **GET** `/health`  
   - Health check endpoint (verifies service is running).

2. **POST** `/export_template`  
   - Exports a QRM template (e.g. to an Excel file).

3. **POST** `/import_template`  
   - Imports a template (Excel) into QRM with updated data.

4. **POST** `/run_saved_workflow`  
   - Runs a saved workflow in QRM (predefined set of steps).

5. **POST** `/get_qrm_run_progress_summary`  
   - Gets the run progress summary (e.g. status of a long-running QRM job).

6. **GET** `/list_db`  
   - Lists available QRM databases.

7. **GET** `/scripting_dll`  
   - Possibly returns or checks the scripting DLL info used by QRM.

8. **GET** `/list_scenario`  
   - Retrieves available QRM scenarios.

9. **GET** `/list_run_params`  
   - Lists potential run parameters (markets, assumption sets, etc.).

10. **GET** `/list_strategy`  
    - Shows available strategies in QRM.

11. **GET** `/structure_change_check`  
    - Possibly checks whether structural changes are required or have happened in QRM.

---

## 7. **Example PowerShell Logic**

Below is a simplified snippet (as seen in the images) showing how the PowerShell script might call QRM’s DLL methods. The Python code dynamically populates variables like `$DatabaseName`, `$StrategyName`, `$Component`, `$PortfolioName`, `$XLSPath`, etc.

```powershell
$DatabaseName = "<export_database_name>"
$CAUrl = "<export_ca_uri>"
#Export QRM Components

if ($objQRM.Login($DatabaseName)) {
  Write-Host "Login for database $DatabaseName succeeded"
} else {
  CleanUpAndExit("Login for database $DatabaseName failed - " + $objQRM.cErrMsg)
}

# Example of setting portfolio, market, assumption sets, run params, etc.
if ($objQRM.SetAssumptionSet($AssumptionSet)) {
  Write-Host "Select for AssumptionSet [$AssumptionSet] successful"
} else {
  CleanUpAndExit("Select for AssumptionSet [$AssumptionSet] failed: " + $objQRM.cErrMsg)
}

# Execute the Export (or any QRM function)
try {
  $result = $objQRM.ExportPlanningStrategy($StrategyName, $Component, $PortfolioName, $XLSPath)
  Write-Output "Result: $result"
} catch {
  Write-Output "An error occurred: $_"
} finally {
  Write-Output "Execution of ExportPlanningStrategy completed"
}
```

**Notes**:  
- The Python code injects the actual parameter values in place of `<export_database_name>`, `<StrategyName>`, etc.  
- The wrapper logs success or error messages. If errors are cryptic, deeper debugging might involve running the same script **interactively** from the server.

---

## 8. **Transition & Next Steps**

1. **Transition**:  
   - Ownership is moving to the official QRM team since their bandwidth has improved.  
   - The original authors are preparing a detailed handoff.  

2. **Handoff Items**:
   - **Code repository**: GitHub URL, branches, and any build scripts.  
   - **Deployment documentation**: Step-by-step instructions for zipping, copying, and restarting the service.  
   - **Configuration and placeholders**: Example environment config files, script placeholders, etc.  
   - **Contacts**: L2/L3 support and relevant QRM experts (e.g., Jay Chapman) who can run interactive tests on the server.  

3. **Timeline**:  
   - Both teams will set up knowledge-transfer sessions as needed.  
   - The new team can decide whether or when to introduce advanced changes (e.g., new logging approaches, re-platforming, or authentication in the wrapper).

---

## 9. **Key Takeaways and Reminders**
- **Critical Constraints**: QRM accessibility is **highly restricted** (firewall, licensing, location).  
- **Python+PowerShell** is a workaround for **no direct QRM API**.  
- **Manual Deployments** are required on an on‑prem Windows server; no PCF or standard CI/CD pipeline.  
- **Logs** are crucial for troubleshooting because many developers cannot RDP to the server.  
- **The Wrapper** is only **one** component in a broader “orchestration” that also interacts with FAST, databases, and other systems to automate the full forecasting workflow.

---

### Final Words
This single consolidated overview should give any new stakeholder a **complete end-to-end picture** of the QRM wrapper’s purpose, architecture, endpoints, deployment steps, and future handoff plan—**including** details on the PowerShell scripts, logs, and the Swagger API calls as requested.