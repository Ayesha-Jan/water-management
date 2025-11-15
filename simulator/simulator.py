import time, json, random, ssl
import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 8883
topic = "water/sensor"

client = mqtt.Client()
client.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS_CLIENT)
client.tls_insecure_set(False)
client.connect(broker, port)

# Define 3 sensors with fixed coordinates
sensors = [
    {"device_id": "sensor_berlin_center", "latitude": 52.520, "longitude": 13.405},  # Berlin Mitte
    {"device_id": "sensor_berlin_north", "latitude": 52.567, "longitude": 13.415},   # Prenzlauer Berg
    {"device_id": "sensor_berlin_south", "latitude": 52.457, "longitude": 13.381},   # Tempelhof
]

while True:
    for sensor in sensors:
        # Generate fake data
        payload = {
            "device_id": sensor["device_id"],
            "flow_rate": round(random.uniform(0.0, 12.0), 2),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "latitude": sensor["latitude"],
            "longitude": sensor["longitude"]
        }
        print("Sending:", payload)
        client.publish(topic, json.dumps(payload))
        time.sleep(2)
    time.sleep(5)