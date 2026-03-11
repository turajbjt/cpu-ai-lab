import json
import os

MEMORY_FILE = "learning/lessons.json"

def save_lesson(goal: str, lesson: str) -> None:
    if not os.path.exists(MEMORY_FILE):
        data = []
    else:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)

    data.append({"goal": goal, "lesson": lesson})

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)
