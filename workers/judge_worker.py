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
        "judge"
    )

    article = load_artifact(
        job_id,
        "rewrite.md"
    )

    prompt_template = load_prompt(
        "judge"
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

        scores = json.loads(
            cleaned
        )

    except Exception as e:

        print(
            f"[JUDGE PARSE ERROR] {e}"
        )

        save_json(
            job_id,
            "judge_raw.json",
            {
                "response": result
            }
        )

        scores = {
            "scores": {
                "clarity": 0,
                "accuracy": 0,
                "engagement": 0,
                "structure": 0,
                "accessibility": 0,
                "seo": 0
            },
            "overall": 0,
            "recommendation": "fail",
            "issues": [],
            "raw_response": result
        }

    save_json(
        job_id,
        "judge.json",
        scores
    )

    return scores