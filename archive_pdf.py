from pathlib import Path
import shutil


ARCHIVE_DIR = Path("archive")


def archive_pdf(pdf_path):

    ARCHIVE_DIR.mkdir(
        exist_ok=True
    )

    pdf_path = Path(pdf_path)

    destination = (
        ARCHIVE_DIR /
        pdf_path.name
    )

    shutil.move(
        str(pdf_path),
        str(destination)
    )