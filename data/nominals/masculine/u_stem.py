from utils import *

BASE_STEM = {
    "singular": [
        "s",
        f"[am]({sutra_link('6.1.107')}) = -m",
        f"[ā]({sutra_link('7.3.120')}) <br> -nā",
        f" [guṇa-u(o)]({sutra_link('7.3.111')}) + e <br> = -ave",
        f" [guṇa-u(o)]({sutra_link('7.3.111')}) + -[as]({sutra_link('6.1.110')}) <br> = -os",
        f" [guṇa-u(o)]({sutra_link('7.3.111')}) + -[as]({sutra_link('6.1.110')}) <br> = -os",
        f" [i]({sutra_link('7.3.119')}) <br> = -au",
        f"[guṇa-u(o)]({sutra_link('7.3.108')}) + [s]({sutra_link('6.1.69')}) <br>= o"
    ],
    "dual": [
        f"-[au]({sutra_link('6.1.102')})<br> = ū",
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
    "singular": ["vāyuḥ", "vāyum", "vāyunā", "vāyave", "vāyoḥ", "vāyoḥ", "vāyau", "vāyo"],
    "dual": ["vāyū", "vāyubhyām", "vāyvoḥ"],
    "plural": ["vāyavaḥ", "vāyūn", "vāyubhiḥ", "vāyubhyaḥ", "vāyūnām", "vāyuṣu"]
}

U_STEM = {
    0: BASE_STEM,
    1: EXAMPLE
}