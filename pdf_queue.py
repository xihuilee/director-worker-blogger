from pathlib import Path

INPUT_DIR = Path("input")


def get_next_pdf():

    pdfs = sorted(
        INPUT_DIR.glob("*.pdf")
    )

    if not pdfs:
        return None

    return pdfs[0]