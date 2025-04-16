import json

with open("./data/ttnet_anomalies.json") as f:
    data = json.load(f)

# Add label = 0 to each entry (normal)
for entry in data:
    entry["label"] = 1

with open("./data/ttnet_anomalies.json", "w") as f:
    json.dump(data, f, indent=2)
