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
        "factcheck"
    )

    article = load_artifact(
        job_id,
        "rewrite.md"
    )

    prompt_template = load_prompt(
        "factcheck"
    )

    prompt = f"""
{prompt_template}

ARTICLE:

{article}
"""

    result = ask(prompt)

    save_artifact(
        job_id,
        "factcheck.md",
        result
    )

    return result