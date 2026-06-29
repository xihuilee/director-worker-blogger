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
        "clean"
    )

    source_text = load_artifact(
        job_id,
        "source.txt"
    )

    prompt = f"""
{load_prompt('clean')}

DOCUMENT:

{source_text}
"""

    result = ask(prompt)

    save_artifact(
        job_id,
        "clean.md",
        result
    )

    return result