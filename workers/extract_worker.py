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
        "extract"
    )

    clean_text = load_artifact(
        job_id,
        "clean.md"
    )

    prompt_template = load_prompt(
        "extract"
    )

    prompt = f"""
{prompt_template}

SOURCE TEXT:

{clean_text}
"""

    result = ask(prompt)

    save_artifact(
        job_id,
        "extract.md",
        result
    )

    return result