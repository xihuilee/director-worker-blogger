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
        "brief"
    )

    extract = load_artifact(
        job_id,
        "extract.md"
    )

    prompt_template = load_prompt(
        "brief"
    )

    prompt = f"""
{prompt_template}

EXTRACTION:

{extract}
"""

    result = ask(prompt)

    save_artifact(
        job_id,
        "brief.md",
        result
    )

    return result