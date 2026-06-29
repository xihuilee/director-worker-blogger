import json
from pathlib import Path


JOBS_DIR = Path("jobs")


def create_job(job_id):

    job_dir = JOBS_DIR / job_id

    job_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    return job_dir


def save_artifact(
    job_id,
    filename,
    content
):

    job_dir = create_job(job_id)

    artifact_file = job_dir / filename

    artifact_file.write_text(
        content,
        encoding="utf-8"
    )

    return artifact_file


def load_artifact(
    job_id,
    filename
):

    artifact_file = (
        JOBS_DIR /
        job_id /
        filename
    )

    if not artifact_file.exists():
        return None

    return artifact_file.read_text(
        encoding="utf-8"
    )

def save_json(
    job_id,
    filename,
    data
):

    job_dir = create_job(job_id)

    file_path = job_dir / filename

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    return file_path

def save_source(
    job_id,
    source_text
):

    save_artifact(
        job_id,
        "source.txt",
        source_text
    )