BASE_LETTERS = "ਸਹਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧਨਪਫਬਭਮਯਰਲਵੜਸ਼ਖ਼ਗ਼ਜ਼ਫ਼ਲ਼"
VOWEL_LETTERS = (
    # ਅ ਆ ਏ ਐ ਇ ਈ ਓ ਔ ਉ ਊ
    "ਅ\u0a06\u0a0f\u0a10\u0a07\u0a08\u0a13\u0a14\u0a09\u0a0a"
)

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

VOWEL_ATTACHMENTS = (
    LEFT_VOWEL_ATTACHMENTS
    + TOP_VOWEL_ATTACHMENTS
    + BOTTOM_VOWEL_ATTACHMENTS
    + RIGHT_VOWEL_ATTACHMENTS
)

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
                ALL_VOWEL_COMBOS.append(
                    f"{left_vowel}{top_vowel}{bottom_vowel}{right_vowel}"
                )
ALL_VOWEL_COMBOS = sorted([*set(ALL_VOWEL_COMBOS)])
