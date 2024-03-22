import streamlit as st
from nominal_forms import get_nominal_form

from pathlib import Path

# Define custom theme
def custom_theme():
    st.set_page_config(
        page_title="My Custom App",
        page_icon=":tada:",  # You can use emoji or image path here
        layout="wide",
    )

def read_markdown_file(filepath):
  """
  This function reads the content of a markdown file.

  Args:
      filepath (str): Path to the markdown file.

  Returns:
      str: Content of the markdown file.
  """
  return Path(filepath).read_text()


custom_theme()

st.header("Sanskrit Reference")
use_devanagari = st.checkbox("Use Devanagari", value=False)
title_headings = {
    "Devanagari" : ["शब्ध रूप", "धातु रूप", "सन्धि"],
    "IAST": ["Nominal Forms", "Verbs Forms", "Euphonic Combinations", "Rules Classfication"]
}

noun_forms, verb_forms, sandhi, rules = st.tabs(title_headings["IAST"])

def sutra_link(sutra:str):
    return f"https://ashtadhyayi.com/sutraani/{sutra}"


with noun_forms:
    genders =  st.tabs(["Masculine","Feminine","Neuter"])



    with genders[0]:
        forms = st.tabs(["a-stem", "i-stem", "u-stem","ṛ-stem","s-stem"])
        for i in range(len(forms)):
            with forms[i]:
                if i == 0:
                    example_stem = {
                        "singular": ["rāmaḥ","rāmam","rāmeṇa","rāmāya","rāmāt","rāmasya","rāme","rāma"],
                        "dual":["rāmau","rāmābhyām","rāmayoḥ"],
                        "plural": ["rāmāḥ","rāmān","rāmaiḥ","rāmebhyaḥ","rāmāṇām","rāmeṣu"]
                    }
                    st.markdown(get_nominal_form(example_stem["singular"],example_stem["dual"],example_stem["plural"], use_devanagari))
                if i == 1:
                    example_stem = {
                        "singular": ["agniḥ", "agnim", "agninā", "agnaye", "agneḥ", "agneḥ", "agnau", "agne"],
                        "dual":["agnī","agnibhyām","agnyoḥ"],
                        "plural": ["agnayaḥ","agnīn","agnibhiḥ","agnibhyaḥ","agnīnām","agniṣu"]
                    }
                    raw_stem = {
                        "singular": [
                            f"-s",
                            f"-am",
                            f"-ā",
                            f"-e",
                            f"-as",
                            f"-as",
                            f"-i",
                            f"-s"
                        ],
                        "dual": [
                            f"-au",
                            f"-bhyām",
                            f"-os"
                        ],
                        "plural": ["-as", "-as", "-bhis", "-bhyas", "-ām", "-su"]
                    }
                    base_stem = {
                        "singular": [
                            "s",
                            f"[am]({sutra_link('6.1.107')}) = -m",
                            f"[ā]({sutra_link('7.3.120')}) <br> -nā",
                            f" [guṇa-i(e)]({sutra_link('7.3.111')}) + e <br> = -aye",
                            f" [guṇa-i(e)]({sutra_link('7.3.111')}) + -[as]({sutra_link('6.1.110')}) <br> = -es",
                            f" [guṇa-i(e)]({sutra_link('7.3.111')}) + -[as]({sutra_link('6.1.110')}) <br> = -es",
                            f" [i]({sutra_link('7.3.119')}) <br> = -au",
                            f"[guṇa-i(e)]({sutra_link("7.3.108")}) + [s]({sutra_link("6.1.69")}) <br>= e"
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
                    st.write("#### General Rule")
                    st.write(f"s/स् in the final form becomes ḥ/ः {sutra_link('8.2.66')},{sutra_link('8.3.15')}", unsafe_allow_html=True)
                    raw, base, example = st.columns([1,1.3,1.2])

                    with raw:
                        st.header("Base")
                        st.markdown(get_nominal_form(raw_stem["singular"], raw_stem["dual"], raw_stem["plural"],
                                                     use_devanagari), unsafe_allow_html=True)
                    with base:
                        st.header("Stem Based Changes")
                        st.markdown(get_nominal_form(base_stem["singular"], base_stem["dual"], base_stem["plural"], use_devanagari), unsafe_allow_html=True)
                    with example:
                        st.header("Example")
                        st.markdown(get_nominal_form(example_stem["singular"],example_stem["dual"],example_stem["plural"], use_devanagari))
                if i == 2:
                    example_stem = {
                        "singular": ["vāyuḥ","vāyum","vāyunā","vāyave","vāyoḥ","vāyoḥ","vāyau","vāyo"],
                        "dual":["vāyū","vāyubhyām","vāyvoḥ"],
                        "plural": ["vāyavaḥ","vāyūn","vāyubhiḥ","vāyubhyaḥ","vāyūnām","vāyuṣu"]
                    }
                    raw_stem = {
                        "singular": ["-ḥ", "-m", "-nā", "-(guṇa u)+e = -o+e = -ave", "-(guṇa u)+ḥ = -oḥ", "-(guṇa u)+ḥ= -oḥ", "-(vṛddhi u) = -au", "-(guṇa u) = -o"],
                        "dual": ["-u", "-bhyām", "-oḥ"],
                        "plural": ["-(guṇa u)+ aḥ = -avaḥ", "-un", "-bhiḥ", "-bhyaḥ", "-unām", "-su"]
                    }
                    base, example = st.columns([1,1])
                    with base:
                        st.markdown(get_nominal_form(raw_stem["singular"], raw_stem["dual"], raw_stem["plural"], use_devanagari), unsafe_allow_html=True)
                    with example:
                        st.markdown(get_nominal_form(example_stem["singular"],example_stem["dual"],example_stem["plural"], use_devanagari))

with sandhi:
    sandhis = st.tabs(["Visarga Sandhi"])

    with sandhis[0]:
        if use_devanagari:
            data = """
            ||कर्कशव्यञ्जनम्|मृदुव्यञ्जनम्|
|:-:|:-:|:-:|
|**कण्ठ्य**|क्, ख्| ग्, घ्, ङ्, ह्|
|**तालव्य**|च्, छ्| ज्, झ्, ञ्, य्|
|**मूर्धन्य**|ट्, ठ्| ड्, ढ्, ण्, र्|
|**दन्त्य** |त्, थ्| द्, ध्, न्, ल्|
|**ओष्ठ्य** |प्, फ्| ब्, भ्, म्, व्|
|**ऊष्मन्**|श् (तालव्य),<br> ष् (मूर्धन्य),<br> स् (दन्त्य)|-|

<br>

|Pre-विसर्ग|Post-विसर्ग| Form | Replacement| Replace/Change Note | Final Form | Example|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|अ|अ| अ+ः+अ| ओऽ| Replace all three| ओऽ |रामः + अत्र = रामोऽत्र|
|अ|Any स्वर except अ| अ+ः+स्वर| -|Removal of विसर्ग|अ+स्वर| शिवः + आसीत् = शिव आसीत्|
|अ|मृदु| अ+ः+मृदु| ओ |ओकार| ओ + मृदु |देवः + राजते = देवो राजते|
|आ|Any स्वर/मृदु| आ+ः+स्वर/मृदु|-| Removal of विसर्ग| आ+ स्वर/मृदु| बालाः + अत्र = बाला अत्र|
|Any स्वर except अ/आ| Any स्वर/मृदु| स्वर + ः + स्वर/मृदु| र् | रकार| स्वर + र् + स्वर/मृदु| कविः + अयम् = कविरयम्|
|Any स्वर except अ/आ| र्| स्वर + ः + र्| दीर्घ of स्वर| Removal of विसर्ग <br> अ-> आ; इ- > ई, <br> उ-> ऊ; ऋ -> ॠ; ऌ->ॡ <br> ए -> ऐ; ओ->औ| दीर्घ स्वर + र्| कविः + राजते = कवी रजते; तैः + रक्षितम् = तै रक्षितम्|
|Any स्वर| कण्ठ्य कर्कश|स्वर +  ः + क्/ख्|ᳵ/ः| जिह्वामूलीय/विसर्ग |ᳵ/ः + क्/ख्|रामः + करोति = रामᳵकरोति/रामः करोति|
|Any स्वर| तालव्य कर्कश |स्वर +  ः + च्/छ्/श्|श्| तालव्य ऊष्मन् |श् + च्/छ्/श्|देवाः + चरति देवाश्चरति|
|Any स्वर| मूर्धन्य कर्कश |स्वर +  ः + ट्/ठ्/ष्|ष्| मूर्धन्य ऊष्मन्|ष् + ट्/ठ्/ष्|रामः + टिकते = रामष्तिकते|
|Any स्वर| दन्त्य कर्कश |स्वर +  ः + त्/थ्/स्|स्| दन्त्य ऊष्मन्|स् + त्/थ्/स्| उन्नतः + तरुः = उन्नतस्तरुः|
|Any स्वर| ओष्ठ्य कर्कश |स्वर +  ः + प्/फ्|ᳶ/ः| उपध्मानीय/विसर्ग|ᳶ/ः + प्/फ्|नः + प्रचोदयात् = नᳶप्रचोदयात्/नः प्रचोदयात्|
|Any स्वर| कर्कश+ऊष्मन्|स्वर +  ः + कर्कश+ऊष्मन्| - | No change <br> Visarga stays|ः + कर्कश+ऊष्मन्| रामः + क्षत्रियः = रामः क्षत्रियः |
|Any स्वर| ऊष्मन्+कर्कश|स्वर +  ः + ऊष्मन्+कर्कश| १. Removal  <br> २. ः <br>३. Same ऊस्मन्| १.The विसर्ग is removed <br> २. The विसर्ग Stays <br> ३. The same ऊष्मन् is replaced| १. ऊष्मन्+कर्कश <br> २. ः + ऊष्मन्+कर्कश <br>३. Same ऊस्मन् + ऊष्मन्+कर्कश | मनः + स्थितिः = मन स्थितिः/मनः स्थितिः/मनस्स्थितिः| 
|सम्बोधन-एकवचन् of ऋकारान्त/अव्यय| र् | स्वर + ः + र्| दीर्ग of स्वर| Visarga is removed and दीर्घ is applied to last स्वर | दीर्घ स्वर + र्| पुनः + रामते = पुना रामते|
|सम्बोधन-एकवचन् of ऋकारान्त/अव्यय| Any स्वर/ मृदु |स्वर + ः + स्वर/मृदु| र् | रकर| स्वर + र् + स्वर/मृदु| पुनः + अत्र = पुनरत्र|
            """
            st.markdown(data, unsafe_allow_html=True)
        else:
            data = """

||karkaśavyañjanam|mṛduvyañjanam|
|:-:|:-:|:-:|
|**kaṇthya**|k, kh| g, gh, ṅ, h|
|**tālavya**|c, ch| j, jh, ñ, y|
|**mūrdhanya**|ṭ, ṭh| ḍ, ḍh, ṇ, r|
|**dantya** |t, th| d, dh, n, l|
|**oṣṭhya** |p, ph| b, bh, m, v|
|**ūṣman**|ś (tālavya),<br> ṣ (mūrdhanya),<br> s (dantya)|-|
<br>

|Pre-Visarga|Post-Visarga| Form| Replacement| Replacement/Change Note | Final Form| Example|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|a|a| a+ḥ+a| o'|Replaces all 3| o' |ramaḥ + atra = ramo'tra|
|a|any svara except a| a+ḥ+svara| -|Removal of Visarga|a+svara| śivaḥ + āsīt = śiva āsīt|
|a|mṛdu| a+ḥ+mṛdu| o |okāra| o + mṛdu |devaḥ + rājate = devo rājate|
|ā|any svara/mṛdu| ā+ḥ+svara/mṛdu|-| Removal of Visarga| ā+ svara/mṛdu| bālāḥ + atra = bālā atra|
|any svara expect a/ā| any svara/ mṛdu| svara + ḥ + svara/mṛdu| r | rakāra| svara + r + svara/mṛdu| kaviḥ + ayam = kavirayam|
|any svara expect a/ā| r| svara + ḥ + r| dīrgha of svara| Removal of Visarga <br> a-> ā; i- > ī, <br> u-> ū; ṛ -> ṝ; ḷ->ḹ <br> e -> ai; o->au| dīrgha svara + r| kaviḥ + rājate = kavī rajate; taiḥ + rakṣitam = tai rakṣitam|
|any svara| kaṇthya karkaśa| ḥ + k/kh|ᳵ/ḥ| jihvāmūlīya/visarga |ᳵ/ḥ + k/kh|rāmaḥ + karoti = ramaᳵkaroti/ramaḥ karoti|
|any svara| tālavya karkaśa | ḥ + c/ch/ś|ś| tālavya ūṣman |ś + c/ch/ś|devāḥ + carati devāścarati|
|any svara| mūrdhanya karkaśa | ḥ + ṭ/ṭh/ṣ|ṣ| mūrdhanya ūṣman|ṣ + ṭ/ṭh/ṣ|rāmaḥ + ṭikate = ramaṣtikate|
|any svara| dantya karkaśa |ḥ + t/th/s|s| dantya ūṣman|s + t/th/s| unnataḥ + taruḥ = unnatastaruḥ|
|any svara| oṣṭhya karkaśa |ḥ + p/ph|ᳶ/ḥ| upadhmānīya/visarga|ᳶ/ḥ + p/ph|naḥ + pracodayāt = naᳶpracodayāt/naḥ pracodayāt|
|any svara| karkaśa+ūṣman|ḥ + karkaśa+ūṣman| - | No Change <br> Visarga Stays|ḥ + karkaśa+ūṣman| ramaḥ + kṣatriyaḥ = ramaḥ kṣatriyaḥ |
|any svara| ūṣman+karkaśa| ḥ + ūṣman+karkaśa| 1. Removal  <br> 2. ḥ <br>3. same ūsman|1. The Visarga is removed <br> 2. The Visarga stays <br> 3. The same ūṣman is replaced| 1. ūṣman+karkaśa <br> 2. ḥ + ūṣman+karkaśa <br>3. same ūsman + ūṣman+karkaśa | manaḥ + sthitiḥ = mana sthitiḥ/manaḥ sthitiḥ/manassthitiḥ| 
|sambodhana-ekavacan of ṛkāra/avyaya| r | svara + ḥ + r| dīrga of svara| Visarga is removed and dīrgha applied to last svara of avyaya| dīrgha svara + r| punaḥ + ramate = punā ramate|
|sambodhana-ekavacan of ṛkāra/avyaya| any svara/ mṛdu |svara + ḥ + svara/mṛdu| r | rakara| svara + r + svara/mṛdu| punaḥ + atra = punaratra|

            """
            st.markdown(data, unsafe_allow_html=True)
# You can add more elements like buttons, charts, etc.
with rules:
    st.markdown("""
1. Vaidic Grammar
     1. [Preposition in Veda](https://ashtadhyayi.com/sutraani/sk3387)
	 2. [Case affix of Div](https://ashtadhyayi.com/sutraani/sk3394)
		1. [Optional Compounds](https://ashtadhyayi.com/sutraani/sk3399)
	3. [Irregular Aorists](https://ashtadhyayi.com/sutraani/sk3403)
		1. [Vaidic Forms](https://ashtadhyayi.com/sutraani/sk3408)
		2. [Vaidic Diversity](https://ashtadhyayi.com/sutraani/sk3419)
	4. [Vaidic Subjunctive](https://ashtadhyayi.com/sutraani/sk3424)
	    1. [Vaidic Infinitive](https://ashtadhyayi.com/sutraani/sk3436)
	    2. [Vaidic Rules](https://ashtadhyayi.com/sutraani/sk3491)
2. Accents
	1. [Accents](https://ashtadhyayi.com/sutraani/sk3650)
	2. [Root-Accents](https://ashtadhyayi.com/sutraani/sk3671)
	3. [Affix Accents](https://ashtadhyayi.com/sutraani/sk3680)
	4. [Accents of Compounds](https://ashtadhyayi.com/sutraani/sk3734)
	5. [Accents of Verbs](https://ashtadhyayi.com/sutraani/sk3934)
      
    """)