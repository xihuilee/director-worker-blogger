import json
from datetime import date

from state import update_stage
from job_manager import (
    load_artifact,
    save_artifact
)


def _safe_load_json(text):

    try:
        return json.loads(text)
    except Exception:
        return {}


def run(job_id):

    update_stage(
        job_id,
        "astro"
    )

    #
    # Load artifacts
    #
    article = load_artifact(
        job_id,
        "final.md"
    )

    metadata = _safe_load_json(
        load_artifact(
            job_id,
            "metadata.json"
        )
    )

    seo = _safe_load_json(
        load_artifact(
            job_id,
            "seo.json"
        )
    )

    #
    # Metadata
    #
    title = metadata.get(
        "title",
        "Untitled Article"
    )

    slug = metadata.get(
        "slug",
        "untitled"
    )

    tags = metadata.get(
        "tags",
        []
    )

    reading_time = metadata.get(
        "reading_time",
        0
    )

    word_count = metadata.get(
        "word_count",
        0
    )

    #
    # SEO
    #
    description = seo.get(
        "meta_description",
        ""
    )

    #
    # Build tag block
    #
    if tags:

        tag_block = ""

        for tag in tags:

            tag_block += f"  - {tag}\n"

    else:

        tag_block = "  - general\n"

    #
    # Astro Markdown
    #
    astro = f"""---
title: "{title}"
description: "{description}"
pubDate: "{date.today().isoformat()}"
author: "AIplosion"
draft: false
slug: "{slug}"
tags:
{tag_block}heroImage: "/images/{slug}.webp"
canonicalURL: ""
readingTime: {reading_time}
wordCount: {word_count}
---

{article}
"""

    save_artifact(
        job_id,
        "astro.md",
        astro
    )

    return astro