from pathlib import Path
import json


class MemoryStore:
    def __init__(self):
        self.base = Path("memory/checkpoints")
        self.base.mkdir(parents=True, exist_ok=True)

    def record(self, event, payload):
        file = self.base / f"{event}.json"

        with open(file, "w") as f:
            json.dump(payload, f, indent=2)

        print(f"[memory] recorded -> {event}")
