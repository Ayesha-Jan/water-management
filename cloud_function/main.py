import base64, json
from google.cloud import bigquery


def process_data(event, context):
    # Decode the Pub/Sub message
    payload = base64.b64decode(event['data']).decode('utf-8')
    data = json.loads(payload)

    device_id = data.get("device_id", "unknown")
    flow = float(data.get("flow_rate", 0))
    timestamp = data.get("timestamp")
    lat = float(data.get("latitude", 0))
    lon = float(data.get("longitude", 0))
    anomaly = flow > 10.0 or flow < 0.1  # simple leak detection

    client = bigquery.Client()
    table_id = "water-management-477509.water_data.flow_readings"

    rows = [{
        "device_id": device_id,
        "flow_rate": flow,
        "timestamp": timestamp,
        "anomaly": anomaly,
        "latitude": lat,
        "longitude": lon
    }]

    errors = client.insert_rows_json(table_id, rows)
    if errors:
        print(f"Error inserting into BigQuery: {errors}")
    else:
        print(f"Data inserted: {rows}")
