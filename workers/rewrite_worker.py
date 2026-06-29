from llm import ask
from state import update_stage
from job_manager import (
    load_artifact,
    save_artifact
)
from prompt_loader import load_prompt


def run(
    job_id,
    feedback=""
):

    update_stage(
        job_id,
        "rewrite"
    )

    draft = load_artifact(
        job_id,
        "draft.md"
    )

    prompt_template = load_prompt(
        "rewrite"
    )

    prompt = f"""
{prompt_template}

REVIEW FEEDBACK:

{feedback}

ARTICLE:

{draft}
"""

    result = ask(
        prompt
    )

    save_artifact(
        job_id,
        "rewrite.md",
        result
    )

    return result