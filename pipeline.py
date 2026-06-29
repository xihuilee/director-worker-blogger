from workers.clean_worker import run as clean_run
from workers.extract_worker import run as extract_run
from workers.classify_worker import run as classify_run
from workers.brief_worker import run as brief_run
from workers.outline_worker import run as outline_run
from workers.draft_worker import run as draft_run


PIPELINE = [

    ("clean", clean_run),

    ("extract", extract_run),

    ("classify", classify_run),

    ("brief", brief_run),

    ("outline", outline_run),

    ("draft", draft_run),

]