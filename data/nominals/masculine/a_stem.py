from utils import *

BASE_STEM = {
    "singular": [
        "s",
        f"[am]({sutra_link('6.1.107')}) = -m",
        f"[ā]({sutra_link('7.1.12')}) <br> -ina",
        f"[dīrgha-a]({sutra_link('7.3.102')}) + [e]({sutra_link('7.1.13')}) <br> = -āya",
        f" [-as]({sutra_link('7.1.12')}) <br> = -āt",
        f" [-as]({sutra_link('7.1.12')}) <br> = -sya",
        f" -i",
        f"-[s]({sutra_link('6.1.69')})"
    ],
    "dual": [
        f"-[au]({sutra_link('6.1.104')})<br> =  -au",
        f"-bhyām",
        f"-os"
    ],
    "plural": [
        f" [guṇa-u(o)]({sutra_link('7.3.109')}) + as <br> = -avas",
        f" [as]({sutra_link('6.1.102')}) <br> -[ūs]({sutra_link('6.1.103')}) <br> = -ūn",
        f"-bhis",
        f"-bhyas",
        f"-[ām]({sutra_link('7.1.54')}) <br>-[nām]({sutra_link('6.4.3')}) <br> = -ūnām",
        f"-su"]
}


EXAMPLE = {
    "singular": ["rāmaḥ", "rāmam", "rāmeṇa", "rāmāya", "rāmāt", "rāmasya", "rāme", "rāma"],
    "dual": ["rāmau", "rāmābhyām", "rāmayoḥ"],
    "plural": ["rāmāḥ", "rāmān", "rāmaiḥ", "rāmebhyaḥ", "rāmāṇām", "rāmeṣu"]
}

A_STEM = {
    0: BASE_STEM,
    1: EXAMPLE,
}


