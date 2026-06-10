# Semantic Aware Cyber Digital Twin (SA CDT) — Supply Chain Monitoring Dashboard

A real time, multi node Cyber Digital Twin (CDT) monitoring dashboard engineered specifically for critical agri food supply chains. This system serves as a live virtual replica of distributed industrial nodes, implementing high frequency state synchronization, threshold driven anomaly detection, and continuous state mirroring.

## Project Overview & Research Context
This prototype implements the core **Digital Twin Mirroring & Visualization Layer** of a larger proposed **Semantic Aware Cyber Digital Twin (SA CDT)** architecture. It acts as a digital mirror for physical agri food infrastructure, continuously tracking process telemetry, environmental boundaries, and edge computing health metrics to provide immediate operational awareness.

This dashboard represents a foundational component for the **ARDÚ Doctoral Scholarship 2026** research proposal under the supervision of **Dr. Mansoor Ahmed** at **Maynooth University (ADAPT Centre)**. 

### Architectural Mapping:
1. **Physical Edge Layer:** Simulated IoT multi sensor array operating at the supply chain edge.
2. **Digital Twin Layer:** This dashboard — executing real time state mirroring, virtual telemetry mapping, and temporal logging.
3. **Analytical Filter Layer:** Deterministic rule based severity classification (`CRITICAL` and `WARNING`).
4. **Next Research Phase:** Integrating a Semantic Web Reasoning Layer (OWL 2 DL, RDF, and SWRL rules via Apache Jena) to close the cyber physical semantic gap and contextually distinguish genuine cyberattacks from benign equipment failures.

---

## Monitored Topology & Boundary Conditions

The framework concurrently simulates and mirrors four heterogeneous nodes critical to the Irish and global meat dairy logistics lifecycle:

| Node Type | Supply Chain Stage | Core Responsibility / Process Monitored |
| :--- | :--- | :--- |
| **Dairy Processing Plant A** | Primary Processing | Pasteurization, vat monitoring, and processing throughput |
| **Cold Storage Warehouse B** | Warehouse Storage | Cold chain preservation integrity and ambient climate control |
| **Refrigerated Transport C** | Logistics & Distribution | In transit asset protection and mobile sensor telemetry |
| **Distribution Hub D** | Retail Logistics | Final mile inventory reception and regional dispatch security |

### Telemetry & Resource Boundaries Checked:
* **Temperature:** Cold chain validation bounds **(Safe Zone: 1°C – 8°C)**.
* **Humidity:** Environmental degradation control **(Safe Zone: 55% – 85%)**.
* **Atmospheric Pressure:** Storage enclosure vacuum verification **(Safe Zone: 95 kPa – 105 kPa)**.
* **CPU Load:** Edge gateway controller health and denial of service indicator **(Safe Zone: 0% – 80%)**.
* **Network Traffic:** Inbound Outbound bandwidth tracking for anomaly signature filtering **(Safe Zone: 0 KB/s – 900 KB/s)**.

---

## Core Technical Capabilities
* **High Frequency Synchronization:** Implements a distributed state monitoring engine featuring a rigid **six second synchronization cycle** to simulate near instantaneous physical to digital state updates.
* **Dual Tier Severity Classification:** Automated evaluation of raw incoming telemetry against safe boundary thresholds, instant triggering of visual states based on `WARNING` and `CRITICAL` breach definitions[cite: 5].
* **Asynchronous Logging:** Non blocking event logging mechanism that generates timestamped, audit ready records of all boundary violations.
* **Responsive Visual Analytics:** Real time data streaming into a dynamic UI, using asynchronous frontend polling and `Chart.js` for real time trend analytics[cite: 5].

---

## Tech Stack & Architecture

* **Backend Engine:** Python, Flask (Micro framework hosting the synchronization routing and telemetry simulation engines)
* **Frontend Dashboard:** HTML5, CSS3 (Tailored Industrial UI Layout), Vanilla JavaScript (Asynchronous DOM state updating)
* **Data Visualization:** Chart.js (Real time multi axis time series visualization)
* **Simulation Layer:** High fidelity Python mathematical sensor models tracking randomized walk variants within industrial boundaries.

---

## Deployment & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/AsadRaza067/agri-food-digital-twin-dashboard.git](https://github.com/AsadRaza067/agri-food-digital-twin-dashboard.git)
cd agri-food-digital-twin-dashboard
