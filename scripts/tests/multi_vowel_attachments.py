from scripts.constants import (
    ALL_VOWEL_COMBOS,
    BASE_LETTER_MODIFIERS,
    BASE_LETTERS,
    BELOW_LETTERS,
    BELOW_LETTERS_EXTENDED,
    VIRAMA,
)

mva_items = []

# for every letter, show every multi-vowel combo on every akhand/modifier
for letter in BASE_LETTERS:
    for akhand in BELOW_LETTERS + BELOW_LETTERS_EXTENDED:
        str = ""
        str += f"{letter}{VIRAMA}{akhand} "
        for vowel_combo in ALL_VOWEL_COMBOS:
            str += f"{letter}{VIRAMA}{akhand}{vowel_combo} "
        mva_items.append(
            {"item": str, "description": f"{letter}{VIRAMA}{akhand} attachments"}
        )

    for modifier in BASE_LETTER_MODIFIERS:
        str = ""
        str += f"{letter}{modifier} "
        for vowel_combo in ALL_VOWEL_COMBOS:
            str += f"{letter}{modifier}{vowel_combo} "
        mva_items.append(
            {"item": str, "description": f"{letter}{modifier} attachments"}
        )
