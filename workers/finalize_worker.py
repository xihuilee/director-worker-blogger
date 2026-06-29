import json

from llm import ask
from state import update_stage
from job_manager import (
    load_artifact,
    save_artifact
)
from prompt_loader import load_prompt


def run(job_id):

    update_stage(
        job_id,
        "finalize"
    )

    article = load_artifact(
        job_id,
        "rewrite.md"
    )

    judge = load_artifact(
        job_id,
        "judge.json"
    )

    prompt_template = load_prompt(
        "finalize"
    )

    prompt = f"""
{prompt_template}

JUDGE RESULTS:

{judge}

ARTICLE:

{article}
"""

    result = ask(prompt)

    save_artifact(
        job_id,
        "final.md",
        result
    )

    return result