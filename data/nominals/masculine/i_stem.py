from utils import sutra_link

BASE_STEM = {
    "singular": [
        "s",
        f"[am]({sutra_link('6.1.107')}) = -m",
        f"[ā]({sutra_link('7.3.120')}) <br> -nā",
        f" [guṇa-i(e)]({sutra_link('7.3.111')}) + e <br> = -aye",
        f" [guṇa-i(e)]({sutra_link('7.3.111')}) + -[as]({sutra_link('6.1.110')}) <br> = -es",
        f" [guṇa-i(e)]({sutra_link('7.3.111')}) + -[as]({sutra_link('6.1.110')}) <br> = -es",
        f" [i]({sutra_link('7.3.119')}) <br> = -au",
        f"[guṇa-i(e)]({sutra_link('7.3.108')}) + [s]({sutra_link('6.1.69')}) <br>= e"
    ],
    "dual": [
        f"-[au]({sutra_link('6.1.102')})<br> = ī",
        f"-bhyām",
        f"-os"
    ],
    "plural": [
        f" [guṇa-i(e)]({sutra_link('7.3.109')}) + as <br> = -ayas",
        f" [as]({sutra_link('6.1.102')}) <br> -[īs]({sutra_link('6.1.103')}) <br> = -īn",
        f"-bhis",
        f"-bhyas",
        f"-[ām]({sutra_link('7.1.54')}) <br>-[nām]({sutra_link('6.4.3')}) <br> = -īnām",
        f"-su"]
}

EXAMPLE = {
    "singular": ["agniḥ", "agnim", "agninā", "agnaye", "agneḥ", "agneḥ", "agnau", "agne"],
    "dual": ["agnī", "agnibhyām", "agnyoḥ"],
    "plural": ["agnayaḥ", "agnīn", "agnibhiḥ", "agnibhyaḥ", "agnīnām", "agniṣu"]
}

I_STEM = {
    0: BASE_STEM,
    1: EXAMPLE
}
