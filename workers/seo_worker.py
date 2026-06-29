import json

from llm import ask
from state import update_stage

from job_manager import (
    load_artifact,
    save_json
)

from prompt_loader import load_prompt


def run(job_id):

    update_stage(
        job_id,
        "seo"
    )

    article = load_artifact(
        job_id,
        "final.md"
    )

    prompt_template = load_prompt(
        "seo"
    )

    prompt = f"""
{prompt_template}

ARTICLE:

{article}
"""

    result = ask(
        prompt
    )

    try:

        cleaned = result.strip()

        if cleaned.startswith(
            "```json"
        ):
            cleaned = cleaned.replace(
                "```json",
                "",
                1
            )

        if cleaned.endswith(
            "```"
        ):
            cleaned = cleaned[:-3]

        cleaned = cleaned.strip()

        seo_data = json.loads(
            cleaned
        )

    except Exception as e:

        print(
            f"[SEO PARSE ERROR] {e}"
        )

        seo_data = {
            "title": "",
            "meta_description": "",
            "slug": "",
            "keywords": [],
            "raw_response": result
        }

    save_json(
        job_id,
        "seo.json",
        seo_data
    )

    return seo_data