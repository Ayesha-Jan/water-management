from google.cloud import pubsub_v1
import paho.mqtt.client as mqtt
import ssl

project_id = "water-management-477509"
topic_id = "water-sensor-topic"
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)


def on_message(client, userdata, msg):
    data = msg.payload.decode()
    print(f"Received MQTT message: {data}")
    publisher.publish(topic_path, data.encode("utf-8"))


client = mqtt.Client()
client.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS_CLIENT)
client.tls_insecure_set(False)
client.connect("broker.hivemq.com", 8883)
client.subscribe("water/sensor")
client.on_message = on_message

print("Bridge running...")
client.loop_forever()
