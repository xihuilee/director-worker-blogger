from datetime import datetime


def generate_job_id():

    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )