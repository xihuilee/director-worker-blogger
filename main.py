from director.director import run as director_run

from job_id import generate_job_id
from pdf_ingest import extract_text

from job_manager import save_source
from pdf_queue import get_next_pdf

from archive_pdf import archive_pdf


def main():

    while True:

        pdf_path = get_next_pdf()

        if pdf_path is None:

            print("[MAIN] No PDFs Found")
            break

        source_text = extract_text(
            pdf_path
        )

        job_id = generate_job_id()

        print(
            f"[MAIN] Starting Job {job_id}"
        )

        print(
            f"[MAIN] Processing PDF: {pdf_path}"
        )

        save_source(
            job_id,
            source_text
        )

        director_run(
            job_id=job_id,
            source_text=source_text
        )

        archive_pdf(
            pdf_path
        )

        print(
            f"[MAIN] Finished Job {job_id}"
        )


if __name__ == "__main__":
    main()