from flask import Flask, jsonify
from pathlib import Path
import random
from datetime import datetime
from collections import deque

app = Flask(__name__)

# ── State ─────────────────────────────────────────────────────────────────────
history = deque(maxlen=50)

NODES = [
    {"id": "NODE-01", "name": "Dairy Processing Plant A", "type": "Processing"},
    {"id": "NODE-02", "name": "Cold Storage Warehouse B", "type": "Storage"},
    {"id": "NODE-03", "name": "Refrigerated Transport C", "type": "Transport"},
    {"id": "NODE-04", "name": "Distribution Hub D",       "type": "Distribution"},
]

THRESHOLDS = {
    "temperature": {"min": 1.0,  "max": 8.0},
    "humidity":    {"min": 55.0, "max": 85.0},
    "pressure":    {"min": 95.0, "max": 105.0},
    "cpu_load":    {"min": 0.0,  "max": 80.0},
    "network_in":  {"min": 0.0,  "max": 900.0},
}

def simulate_node(node, force_anomaly=False):
    anomaly = force_anomaly or (random.random() < 0.08)
    if anomaly:
        temp     = round(random.uniform(10.0, 20.0), 2)
        humidity = round(random.uniform(20.0, 50.0), 2)
        pressure = round(random.uniform(80.0, 93.0), 2)
        cpu      = round(random.uniform(85.0, 99.0), 2)
        net_in   = round(random.uniform(950.0, 1500.0), 2)
    else:
        temp     = round(random.uniform(2.0, 7.5), 2)
        humidity = round(random.uniform(58.0, 83.0), 2)
        pressure = round(random.uniform(96.0, 104.0), 2)
        cpu      = round(random.uniform(10.0, 75.0), 2)
        net_in   = round(random.uniform(50.0, 850.0), 2)

    alerts = []
    if not (THRESHOLDS["temperature"]["min"] <= temp <= THRESHOLDS["temperature"]["max"]):
        alerts.append({"metric": "Temperature", "value": f"{temp}°C",
                       "safe": "1–8°C", "severity": "CRITICAL"})
    if not (THRESHOLDS["humidity"]["min"] <= humidity <= THRESHOLDS["humidity"]["max"]):
        alerts.append({"metric": "Humidity", "value": f"{humidity}%",
                       "safe": "55–85%", "severity": "WARNING"})
    if not (THRESHOLDS["pressure"]["min"] <= pressure <= THRESHOLDS["pressure"]["max"]):
        alerts.append({"metric": "Pressure", "value": f"{pressure} kPa",
                       "safe": "95–105 kPa", "severity": "WARNING"})
    if not (THRESHOLDS["cpu_load"]["min"] <= cpu <= THRESHOLDS["cpu_load"]["max"]):
        alerts.append({"metric": "CPU Load", "value": f"{cpu}%",
                       "safe": "0–80%", "severity": "WARNING"})
    if not (THRESHOLDS["network_in"]["min"] <= net_in <= THRESHOLDS["network_in"]["max"]):
        alerts.append({"metric": "Network Traffic", "value": f"{net_in} KB/s",
                       "safe": "0–900 KB/s", "severity": "CRITICAL"})

    return {
        "node_id":     node["id"],
        "node_name":   node["name"],
        "node_type":   node["type"],
        "timestamp":   datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": temp,
        "humidity":    humidity,
        "pressure":    pressure,
        "cpu_load":    cpu,
        "network_in":  net_in,
        "status":      "ANOMALY" if alerts else "NORMAL",
        "alerts":      alerts,
    }

def get_all_nodes():
    return [simulate_node(n) for n in NODES]

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return Path("index.html").read_text()

@app.route("/api/twin/snapshot")
def snapshot():
    data = get_all_nodes()
    history.append({"timestamp": datetime.now().strftime("%H:%M:%S"), "nodes": data})
    return jsonify(data)

@app.route("/api/twin/history")
def twin_history():
    return jsonify(list(history))

@app.route("/api/twin/stats")
def stats():
    if not history:
        return jsonify({"snapshots": 0, "total_anomalies": 0, "anomaly_rate": 0,
                        "nodes_at_risk": 0, "nodes_healthy": len(NODES)})
    last = history[-1]["nodes"]
    anomalies = sum(1 for n in last if n["status"] == "ANOMALY")
    total_snaps = len(history)
    all_anomalies = sum(
        sum(1 for n in snap["nodes"] if n["status"] == "ANOMALY")
        for snap in history
    )
    total_checks = total_snaps * len(NODES)
    return jsonify({
        "snapshots":      total_snaps,
        "total_anomalies": all_anomalies,
        "anomaly_rate":   round((all_anomalies / total_checks) * 100, 1) if total_checks else 0,
        "nodes_at_risk":  anomalies,
        "nodes_healthy":  len(NODES) - anomalies,
    })

if __name__ == "__main__":
    for _ in range(15):
        snap = {"timestamp": datetime.now().strftime("%H:%M:%S"), "nodes": get_all_nodes()}
        history.append(snap)
    app.run(debug=True, port=5000)
