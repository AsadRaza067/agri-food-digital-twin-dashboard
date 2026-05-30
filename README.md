# 🌾 Agri-food Supply Chain — Cyber Digital Twin Dashboard

A real-time **Cyber Digital Twin (CDT)** monitoring dashboard for agri-food supply chains — providing a live virtual replica of 4 supply chain nodes with real-time anomaly detection, alert logging, and historical trend visualisation.

## Project Overview

This project implements the **Digital Twin monitoring layer** of a Semantic-Aware CDT architecture for agri-food supply chains. It creates a virtual mirror of physical supply chain nodes — continuously monitoring sensor data, detecting anomalies, and providing operators with real-time situational awareness.

### Supply Chain Nodes Monitored:
| Node | Type |
|---|---|
| Dairy Processing Plant A | Processing |
| Cold Storage Warehouse B | Storage |
| Refrigerated Transport C | Transport |
| Distribution Hub D | Distribution |

### Metrics Monitored Per Node:
-  **Temperature** — cold chain integrity (safe: 1–8°C)
-  **Humidity** — storage conditions (safe: 55–85%)
-  **Atmospheric Pressure** — environment monitoring (safe: 95–105 kPa)
-  **CPU Load** — controller health (safe: 0–80%)
-  **Network Traffic** — anomalous traffic detection (safe: 0–900 KB/s)

##  Research Motivation

This dashboard is a **core prototype** for PhD research on Semantic-Aware Cyber Digital Twins for Agri-food Supply Chains at Maynooth University (Dr. Mansoor Ahmed, ADAPT Centre).

In a full SA-CDT architecture, this dashboard represents:
- **Physical Layer** → IoT sensors on supply chain nodes
- **Digital Twin Layer** → virtual replica with real-time state mirroring
- **Anomaly Detection Layer** → threshold-based breach detection

The next research step is adding a **semantic reasoning layer** (OWL ontology) that interprets anomalies in context — distinguishing sensor faults from cyberattacks.

##  Tech Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Visualisation | Chart.js |
| Twin Simulation | Python sensor models |

##  How to Run

```bash
# 1. Clone the repository
git clone https://github.com/AsadRaza067/agri-food-digital-twin-dashboard.git
cd agri-food-digital-twin-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python app.py

# 4. Open browser
# http://localhost:5000
```

##  Project Structure

```
agri-food-digital-twin-dashboard/
├── app.py              # Flask backend + node simulation + anomaly detection
├── index.html          # Live Digital Twin dashboard
├── requirements.txt    # Dependencies
└── README.md
```

## Future Extensions

- Add OWL ontology semantic reasoning layer
- Integrate real IoT hardware (Raspberry Pi sensors)
- Connect to Supply Chain Threat Classifier (ML anomaly detection)
- Add MQTT protocol for real sensor data ingestion
- Implement federated CDT across multiple supply chain operators

## Related Projects

- [Agri-food IoT Anomaly Monitor](https://github.com/AsadRaza067/agri-iot-anomaly-monitor) — IoT data layer
- [Supply Chain Threat Classifier](https://github.com/AsadRaza067/supply-chain-threat-classifier) — ML threat detection

## Author

**Asad Raza**
BSc Computer Science — BIIT, PMAS Arid Agriculture University Rawalpindi
📧 asadraza0667@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/asad-raza-a007r)
