from llm import ask
from state import update_stage

from job_manager import (
    load_artifact,
    save_json
)

from prompt_loader import load_prompt

import json


def run(job_id):

    update_stage(
        job_id,
        "citation"
    )

    article = load_artifact(
        job_id,
        "rewrite.md"
    )

    prompt_template = load_prompt(
        "citation"
    )

    prompt = f"""
{prompt_template}

ARTICLE:

{article}
"""

    result = ask(
        prompt
    )

    try:

        cleaned = result.strip()

        if cleaned.startswith(
            "```json"
        ):
            cleaned = cleaned.replace(
                "```json",
                "",
                1
            )

        if cleaned.endswith(
            "```"
        ):
            cleaned = cleaned[:-3]

        cleaned = cleaned.strip()

        citations = json.loads(
            cleaned
        )

    except Exception as e:

        print(
            f"[CITATION PARSE ERROR] {e}"
        )

        citations = {
            "claims": [],
            "raw_response": result
        }

    save_json(
        job_id,
        "citations.json",
        citations
    )

    return citations