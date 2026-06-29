from pipeline import PIPELINE

from workers.rewrite_worker import run as rewrite_run
from workers.factcheck_worker import run as factcheck_run
from workers.judge_worker import run as judge_run
from workers.finalize_worker import run as finalize_run
from workers.citation_worker import run as citation_run
from workers.seo_worker import run as seo_run
from workers.metadata_worker import run as metadata_run
from workers.astro_worker import run as astro_run

from config_loader import get_setting
from state import complete_job


def run(job_id, source_text):

    print(f"[DIRECTOR] Job {job_id}")

    #
    # Linear Pipeline
    #
    for stage_name, stage_fn in PIPELINE:

        print(
            f"[DIRECTOR] {stage_name.title()}"
        )

        stage_fn(job_id)

    #
    # Adaptive Rewrite Loop
    #
    pass_score = get_setting(
        "judge_pass_score",
        8.0
    )

    max_attempts = get_setting(
        "max_rewrite_attempts",
        2
    )

    attempt = 0

    best_score = -1
    best_feedback = ""

    while True:

        print("[DIRECTOR] Rewrite")

        rewrite_run(
            job_id,
            feedback=best_feedback
        )

        print("[DIRECTOR] Factcheck")

        factcheck_run(
            job_id
        )

        print("[DIRECTOR] Judge")

        judge = judge_run(
            job_id
        )

        score = judge.get(
            "overall",
            0
        )

        recommendation = judge.get(
            "recommendation",
            "fail"
        )

        print(
            f"[JUDGE] Overall: {score}"
        )

        if score > best_score:

            best_score = score

            print(
                f"[DIRECTOR] New Best Score: {best_score}"
            )

        #
        # Success
        #
        if (
            recommendation == "pass"
            or score >= pass_score
        ):

            print(
                "[DIRECTOR] Judge Passed"
            )

            break

        #
        # Maximum Attempts
        #
        attempt += 1

        if attempt >= max_attempts:

            print(
                "[DIRECTOR] Max Rewrite Attempts Reached"
            )

            break

        #
        # Build feedback
        #
        issues = judge.get(
            "issues",
            []
        )

        feedback_lines = []

        for issue in issues:

            severity = issue.get(
                "severity",
                "medium"
            ).upper()

            fix = issue.get(
                "fix",
                ""
            )

            feedback_lines.append(
                f"[{severity}] {fix}"
            )

        best_feedback = "\n".join(
            feedback_lines
        )

        print(
            "[DIRECTOR] Rewrite Feedback:"
        )

        print(
            best_feedback
        )

    #
    # Finalize
    #
    print("[DIRECTOR] Finalize")

    finalize_run(
        job_id
    )

    #
    # Citation
    #
    print("[DIRECTOR] Citation")

    citation_run(
        job_id
    )

    #
    # SEO
    #
    print("[DIRECTOR] SEO")

    seo_run(
        job_id
    )

    #
    # Metadata
    #
    print("[DIRECTOR] Metadata")

    metadata_run(
        job_id
    )

    #
    # Astro Export
    #
    print("[DIRECTOR] Astro")

    astro_run(
        job_id
    )

    print(
        "[DIRECTOR] Complete"
    )

    complete_job()