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
        "metadata"
    )

    article = load_artifact(
        job_id,
        "final.md"
    )

    prompt_template = load_prompt(
        "metadata"
    )

    prompt = f"""
{prompt_template}

ARTICLE:

{article}
"""

    result = ask(prompt)

    #
    # Validate JSON
    #
    try:

        metadata = json.loads(
            result
        )

    except Exception:

        metadata = {
            "title": "",
            "slug": "",
            "excerpt": "",
            "meta_description": "",
            "category": "",
            "tags": []
        }

    save_artifact(
        job_id,
        "metadata.json",
        json.dumps(
            metadata,
            indent=2
        )
    )

    return metadata