# 💧 Smart Water Management System

---

## Description
A real-time IoT-to-Cloud water management system to monitor water flow, detect leaks, and prevent wastage.  
Virtual water sensors send data via MQTT to Google Cloud, where anomalies are detected and visualized in Looker Studio dashboards.

---

## Features
- Virtual water sensors simulate flow readings from multiple locations.
- Real-time anomaly detection:
  - Flow > 10 L/min → possible leak
  - Flow < 0.1 L/min → possible blockage
- MQTT-based communication with TLS encryption.
- Cloud pipeline: MQTT → Pub/Sub → Cloud Functions → BigQuery.
- Looker Studio dashboards for visualization and trend analysis.
- Scalable serverless architecture with pay-per-use cost efficiency.

---

## Files

- `simulator.py` — Simulates virtual water sensors and publishes data via MQTT.  
- `mqtt_to_pubsub.py` — Bridges MQTT messages to Google Cloud Pub/Sub.  
- `main.py` — Cloud Function that processes Pub/Sub messages and writes to BigQuery.  
- `requirements.txt` — Python dependencies.   
- `IoT_Smart_Water_Management.pdf` — Final project presentation slides.

---

## Getting Started

### Prerequisites

- Python 3.10+
- Google Cloud Project with Pub/Sub, Cloud Functions, and BigQuery enabled.

### Clone the Repository 
    
    git clone https://github.com/Ayesha-Jan/water-management.git
    cd water-management
    
### Install Dependencies

- `pip install -r requirements.txt`

---

## How To Run

### Cloud Setup

- Deploy cloud function/main.py to process messages and insert into BigQuery.
- Connect Looker Studio to BigQuery to visualize water flow trends and anomalies.

### Run the MQTT Bridge

- `python mqtt_to_pubsub/mqtt_to_pubsub.py`
- Forwards messages from MQTT broker to Google Cloud Pub/Sub.

### Run the Simulator

- `python simulator/simulator.py`
- Generates water flow data for three virtual sensors.
- Publishes JSON messages every 2–5 seconds via MQTT.

---

## Future Work
- Integrate real water sensors
- Add notifications (email/push) for anomalies
- Predict leaks using BigQuery ML
- Optimize edge processing and multi-zone deployments

---

## Author

Developed by: Ayesha A. Jan  
Email: Ayesha.Jan@stud.srh-campus-berlin.de  
Contributors: [Maha Ibrahim](https://github.com/mahaibrahim26), [Anunitha Kommireddy Umasankari](https://github.com/anunithak)  
🎓 BST IoT And Cloud Technology – 2025
