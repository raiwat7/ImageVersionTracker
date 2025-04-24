import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("image_log.json")

def log_metadata(data: dict):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        **data
    }
    if LOG_FILE.exists():
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def read_logs():
    if LOG_FILE.exists():
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []
