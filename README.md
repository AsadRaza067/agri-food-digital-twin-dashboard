# Semantic-Aware Cyber Digital Twin (SA-CDT) Supply Chain Monitoring Dashboard

A real-time, multi-node Cyber Digital Twin (CDT) monitoring dashboard engineered for critical agri-food supply chains. This system serves as a live virtual replica of distributed industrial nodes, enabling continuous state mirroring, anomaly detection, and operational visibility across edge infrastructure.

---

## Project Overview & Research Context

This prototype implements the **Digital Twin Mirroring & Visualization Layer** of a broader **Semantic-Aware Cyber Digital Twin (SA-CDT) architecture**.

It acts as a real-time digital mirror of physical agri-food infrastructure, continuously tracking:

- Environmental telemetry
- Supply chain process states
- Edge computing health metrics

This enables immediate operational awareness and anomaly visibility across distributed logistics systems.

---

## Architectural Mapping

### Physical Edge Layer
Simulated IoT multi-sensor network operating across agri-food supply chain nodes.

### Digital Twin Layer (This System)
Real-time state mirroring engine responsible for:
- Virtual telemetry mapping
- Continuous state synchronization
- Temporal logging of system events

### Analytical Filter Layer
Rule-based anomaly detection system implementing:
- CRITICAL alerts
- WARNING alerts
- Threshold-based evaluation logic

### Future Semantic Layer (Research Extension)
Next phase of the architecture will integrate:

- OWL 2 DL ontologies  
- RDF knowledge graphs  
- SWRL rule reasoning (Apache Jena)

This will enable semantic distinction between:
- Genuine cyberattacks
- Benign equipment failures
- Environmental anomalies

---

## Monitored Topology & Supply Chain Nodes

| Node Type | Supply Chain Stage | Core Responsibility |
|----------|--------------------|---------------------|
| Dairy Processing Plant A | Primary Processing | Pasteurization, vat monitoring, throughput control |
| Cold Storage Warehouse B | Warehouse Storage | Cold chain integrity and temperature regulation |
| Refrigerated Transport C | Logistics & Distribution | In-transit telemetry and asset protection |
| Distribution Hub D | Retail Logistics | Final-mile inventory reception and dispatch |

---

## Telemetry & Monitoring Parameters

- Temperature: 1°C – 8°C (Cold chain integrity)
- Humidity: 55% – 85% (Environmental stability)
- Atmospheric Pressure: 95 kPa – 105 kPa (Storage enclosure validation)
- CPU Load: 0% – 80% (Edge gateway health monitoring)
- Network Traffic: 0 – 900 KB/s (Anomaly signal detection)

---

## Core Technical Capabilities

- High-frequency synchronization using a 6-second update cycle for real-time state mirroring
- Dual-tier severity classification system (**CRITICAL / WARNING**) for anomaly detection
- Asynchronous event logging with timestamped audit trails
- Real-time UI updates using polling-based frontend architecture
- Interactive visualization using Chart.js for time-series monitoring
- Distributed simulation of heterogeneous IoT edge nodes

---

## Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Visualization | Chart.js |
| Simulation | Python stochastic sensor models (random walk-based) |

---

## How to Run

```bash
# 1. Clone repository
git clone https://github.com/AsadRaza067/Semantic-Aware-Cyber-Digital-Twin-SA-CDT-Supply-Chain-Monitoring-Dashboard.git

# 2. Navigate to project
cd Semantic-Aware-Cyber-Digital-Twin-SA-CDT-Supply-Chain-Monitoring-Dashboard

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run application
python app.py

# 5. Open in browser
http://localhost:5000
```

---

## Project Structure

```text
Semantic-Aware-Cyber-Digital-Twin-SA-CDT-Supply-Chain-Monitoring-Dashboard/
│
├── app.py                  # Flask backend — sensor simulation + CDT synchronization engine
├── requirements.txt        # Python dependencies
├── index.html              # Real-time dashboard UI (Chart.js)
└── README.md
```

---

## Research Positioning

This project is part of a broader **Semantic-Aware Cyber Digital Twin (SA-CDT) research pipeline**:

| Stage | Project | Role |
|------|--------|------|
| 1 | Edge Anomaly Detection System | Real-time IoT anomaly detection |
| 2 | Cyber Threat Classification | ML-based multi-class attack detection |
| 3 | Digital Twin Layer (This Project) | Real-time cyber-physical state mirroring |
| 4 | Semantic Reasoning Layer (Future Work) | OWL/RDF-based intelligence layer |

---

## Future Extensions

- Integration of OWL 2 DL semantic reasoning layer  
- RDF-based knowledge graph for supply chain intelligence  
- SWRL rule engine using Apache Jena  
- Real IoT hardware deployment (Raspberry Pi sensor integration)  
- MQTT-based real-time streaming architecture  
- AI-driven predictive anomaly detection layer  

---

## Related Publication

**Real-Time Cyber-Physical Intrusion Detection at the Industrial IoT Edge: A Lightweight Temporal Causal Explainable AI (XAI) Framework**

Raza, A. (2026). Zenodo Preprint.  
DOI: https://doi.org/10.5281/zenodo.20539991

---

## Author

**Asad Raza**  
BSc Computer Science — BIIT, PMAS Arid Agriculture University, Rawalpindi  

📧 asadraza0667@gmail.com  

🔗 LinkedIn  
🔗 GitHub  
