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
        "outline"
    )

    brief = load_artifact(
        job_id,
        "brief.md"
    )

    prompt_template = load_prompt(
        "outline"
    )

    prompt = f"""
{prompt_template}

CONTENT BRIEF:

{brief}
"""

    result = ask(prompt)

    save_artifact(
        job_id,
        "outline.md",
        result
    )

    return result