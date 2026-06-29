import fitz
from pathlib import Path


def extract_text(pdf_path):

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():

        raise FileNotFoundError(
            f"PDF not found: {pdf_path.resolve()}"
        )

    doc = fitz.open(pdf_path)

    pages = []

    for page in doc:
        pages.append(
            page.get_text()
        )

    doc.close()

    return "\n".join(pages)