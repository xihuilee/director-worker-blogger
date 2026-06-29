from pathlib import Path


def load_prompt(name):

    path = Path("prompts") / f"{name}.md"

    return path.read_text(
        encoding="utf-8"
    )