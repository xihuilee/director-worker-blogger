import json


def load_config():

    with open(
        "config.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)

def get_setting(
    key,
    default=None
):

    config = load_config()

    return config.get(
        key,
        default
    )

threshold = get_setting(
    "judge_pass_score"
)