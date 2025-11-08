import time, json, random
import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
port = 8883
topic = "water/sensor"

client = mqtt.Client()
client.connect(broker, port)

while True:
    # generate fake data
    payload = {
        "device_id": "sensor_01",
        "flow_rate": round(random.uniform(0.0, 12.0), 2),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    print("Sending:", payload)
    client.publish(topic, json.dumps(payload))
    time.sleep(5)
