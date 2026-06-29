import json

from llm import ask
from state import update_stage
from job_manager import (
    load_artifact,
    save_json
)
from prompt_loader import load_prompt


def run(job_id):

    update_stage(
        job_id,
        "classify"
    )

    content = load_artifact(
        job_id,
        "extract.md"
    )

    prompt_template = load_prompt(
        "classify"
    )

    prompt = f"""
{prompt_template}

DOCUMENT:

{content}
"""

    result = ask(prompt)

    try:
        classification = json.loads(result)
    except Exception:
        classification = {
            "content_type": "general",
            "confidence": 0.0,
            "reason": "parse failure"
        }

    save_json(
        job_id,
        "classification.json",
        classification
    )

    return classification