import json
from pathlib import Path

STATE_FILE = Path("state.json")


def load_state():

    if not STATE_FILE.exists():

        return {
            "current_job": None,
            "current_stage": None,
            "status": "idle"
        }

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(
            state,
            f,
            indent=4,
            ensure_ascii=False
        )


def update_stage(job_id, stage):

    state = load_state()

    state["current_job"] = job_id
    state["current_stage"] = stage
    state["status"] = "running"

    from datetime import datetime

    state["last_updated"] = datetime.now().isoformat()

    save_state(state)

def complete_job():

    state = load_state()

    state["status"] = "completed"

    save_state(state)