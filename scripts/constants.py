NL = {
    "s": "ਸ",
    "h": "ਹ",
    "k": "ਕ",
    "kh": "ਖ",
    "g": "ਗ",
    "gh": "ਘ",
    "ng": "ਙ",
    "c": "ਚ",
    "ch": "ਛ",
    "j": "ਜ",
    "jh": "ਝ",
    "nj": "ਞ",
    "tt": "ਟ",
    "tth": "ਠ",
    "dd": "ਡ",
    "ddh": "ਢ",
    "nn": "ਣ",
    "t": "ਤ",
    "th": "ਥ",
    "d": "ਦ",
    "dh": "ਧ",
    "n": "ਨ",
    "p": "ਪ",
    "ph": "ਫ",
    "b": "ਬ",
    "bh": "ਭ",
    "m": "ਮ",
    "y": "ਯ",
    "r": "ਰ",
    "l": "ਲ",
    "v": "ਵ",
    "rr": "ੜ",
    "sh": "ਸ਼",
    "x": "ਖ਼",
    "gg": "ਗ਼",
    "z": "ਜ਼",
    "f": "ਫ਼",
    "ll": "ਲ਼",
    "kana": "ਾ",
    "sihari": "ਿ",
    "bihari": "ੀ",
    "aunkar": "ੁ",
    "dulainkar": "ੂ",
    "lava": "ੇ",
    "dulava": "ੈ",
    "hora": "ੋ",
    "kanaura": "ੌ",
    "tippi": "ੰ",
    "bindi": "ਂ",
    "addak": "ੱ",
    "visarga": "ਃ",
    "halant": "੍",
    "udaat": "ੑ",
    "yakash": "ੵ",
    "nukta": "਼",
    "0inf": "₀",
    "1inf": "₁",
    "2inf": "₂",
    "3inf": "₃",
    "4inf": "₄",
    "5inf": "₅",
    "6inf": "₆",
    "7inf": "₇",
    "8inf": "₈",
    "9inf": "₉",
    "vs1": "︀",
    "vs2": "︁",
    "vs3": "︂",
    "vs4": "︃",
    "vs5": "︄",
    "vs6": "︅",
    "vs7": "︆",
    "vs8": "︇",
    "vs9": "︈",
    "aa": "\u0a06",
    "e": "\u0a10",
    "ee": "ਐ",
    "i": "ਇ",
    "ii": "ਈ",
    "o": "ਓ",
    "oo": "ਔ",
    "u": "ਉ",
    "uu": "ਊ",
    "ura": "ੳ",
    "aira": "ਅ",
    "iri": "ੲ",
    "ikoankar": "ੴ",
    "zwnj": "‌",
    "zwj": "‍",
}

BASE_LETTERS = "ਸਹਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧਨਪਫਬਭਮਯਰਲਵੜਸ਼ਖ਼ਗ਼ਜ਼ਫ਼ਲ਼"
VOWEL_LETTERS = (
    # ਅ ਆ ਏ ਐ ਇ ਈ ਓ ਔ ਉ ਊ
    "ਅ\u0a06\u0a0f\u0a10\u0a07\u0a08\u0a13\u0a14\u0a09\u0a0a"
)
HALF_LETTERS = [
    f"{NL['vs1']}{NL['th']}",
    f"{NL['vs1']}{NL['m']}",
]
YAYYA_LETTERS = [
    f"{NL['vs1']}{NL['y']}",
    f"{NL['vs2']}{NL['y']}",
    f"{NL['vs1']}{NL['vs2']}{NL['y']}",
]
MAHAN_KOSH_LETTERS = [
    f"{NL['vs5']}{NL['k']}",
    f"{NL['vs2']}{NL['vs5']}{NL['k']}",
    f"{NL['vs4']}{NL['s']}",
    f"{NL['vs4']}{NL['vs5']}{NL['s']}",
    f"{NL['vs6']}{NL['s']}",
    f"{NL['vs8']}{NL['s']}",
    f"{NL['vs5']}{NL['dh']}",
    f"{NL['vs6']}{NL['j']}",
    f"{NL['vs7']}{NL['j']}",
    f"{NL['vs8']}{NL['j']}",
    f"{NL['vs9']}{NL['j']}",
    f"{NL['j']}{NL['halant']}{NL['nj']}",
]

LEFT_VOWEL_ATTACHMENTS = [
    "ਿ",
]

TOP_VOWEL_ATTACHMENTS = [
    "ੇ",
    "ੈ",
    "ੋ",
    "ੌ",
]

BOTTOM_VOWEL_ATTACHMENTS = [
    "ੁ",
    "ੂ",
]

RIGHT_VOWEL_ATTACHMENTS = [
    "ਾ",
    "ੀ",
]

VOWEL_ATTACHMENTS = LEFT_VOWEL_ATTACHMENTS + TOP_VOWEL_ATTACHMENTS + BOTTOM_VOWEL_ATTACHMENTS + RIGHT_VOWEL_ATTACHMENTS

VIRAMA = "੍"
BELOW_LETTERS = "ਹਰਵਟਤਨਚ"
BELOW_LETTERS_EXTENDED = "ਕਠ"

BASE_LETTER_MODIFIERS = [
    "਼",
    "ੑ",
    "ੵ",
]

FINAL_MODIFIERS = [
    "ਁ",
    "ੱ",
    "ਂ",
    "ੰ",
]

VISARGA = "ਃ"


"""
Programmatic constants below
"""

# ALL_VOWEL_COMBOS
ALL_VOWEL_COMBOS = []
for left_vowel in LEFT_VOWEL_ATTACHMENTS:
    ALL_VOWEL_COMBOS.append(f"{left_vowel}")
    for top_vowel in TOP_VOWEL_ATTACHMENTS:
        ALL_VOWEL_COMBOS.append(f"{top_vowel}")
        ALL_VOWEL_COMBOS.append(f"{left_vowel}{top_vowel}")
        for bottom_vowel in BOTTOM_VOWEL_ATTACHMENTS:
            ALL_VOWEL_COMBOS.append(f"{bottom_vowel}")
            ALL_VOWEL_COMBOS.append(f"{left_vowel}{bottom_vowel}")
            ALL_VOWEL_COMBOS.append(f"{top_vowel}{bottom_vowel}")
            ALL_VOWEL_COMBOS.append(f"{left_vowel}{top_vowel}{bottom_vowel}")
            for right_vowel in RIGHT_VOWEL_ATTACHMENTS:
                ALL_VOWEL_COMBOS.append(f"{right_vowel}")
                ALL_VOWEL_COMBOS.append(f"{left_vowel}{right_vowel}")
                ALL_VOWEL_COMBOS.append(f"{top_vowel}{right_vowel}")
                ALL_VOWEL_COMBOS.append(f"{bottom_vowel}{right_vowel}")
                ALL_VOWEL_COMBOS.append(f"{left_vowel}{top_vowel}{right_vowel}")
                ALL_VOWEL_COMBOS.append(f"{left_vowel}{bottom_vowel}{right_vowel}")
                ALL_VOWEL_COMBOS.append(f"{top_vowel}{bottom_vowel}{right_vowel}")
                ALL_VOWEL_COMBOS.append(f"{left_vowel}{top_vowel}{bottom_vowel}{right_vowel}")
ALL_VOWEL_COMBOS = sorted([*set(ALL_VOWEL_COMBOS)])
