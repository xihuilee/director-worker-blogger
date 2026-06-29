import json

from llm import ask
from state import update_stage

from job_manager import (
    load_artifact,
    save_artifact,
    save_json
)

from prompt_loader import load_prompt


def run(job_id):

    update_stage(
        job_id,
        "image_prompt"
    )

    article = load_artifact(
        job_id,
        "final.md"
    )

    prompt_template = load_prompt(
        "image_prompt"
    )

    prompt = f"""
{prompt_template}

ARTICLE:

{article}
"""

    result = ask(prompt)

    try:

        cleaned = result.strip()

        if cleaned.startswith("```json"):
            cleaned = cleaned.replace(
                "```json",
                "",
                1
            )

        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]

        cleaned = cleaned.strip()

        data = json.loads(
            cleaned
        )

    except Exception:

        data = {
            "featured_image": "",
            "sections": []
        }

    save_artifact(
        job_id,
        "featured_image_prompt.txt",
        data.get(
            "featured_image",
            ""
        )
    )

    save_json(
        job_id,
        "section_image_prompts.json",
        {
            "sections": data.get(
                "sections",
                []
            )
        }
    )

    return data