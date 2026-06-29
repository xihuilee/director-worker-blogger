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
        "draft"
    )

    outline = load_artifact(
        job_id,
        "outline.md"
    )

    prompt_template = load_prompt(
        "draft"
    )

    prompt = f"""
{prompt_template}

ARTICLE OUTLINE:

{outline}
"""

    result = ask(prompt)

    save_artifact(
        job_id,
        "draft.md",
        result
    )

    return result