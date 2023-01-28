from scripts.constants import (
    BASE_LETTERS,
    VOWEL_LETTERS,
    VOWEL_ATTACHMENTS,
    VIRAMA,
    BELOW_LETTERS,
    BELOW_LETTERS_EXTENDED,
    BASE_LETTER_MODIFIERS,
    FINAL_MODIFIERS,
    VISARGA,
)

ma_items = []

# show the same vowel on every consonant
for vowel in VOWEL_ATTACHMENTS:
    str = ""
    for letter in BASE_LETTERS:
        str += f"{letter}{vowel} "
    ma_items.append({"item": str, "description": f"{vowel} attachment"})

# show the same akhand on every consonant
for akhand in BELOW_LETTERS + BELOW_LETTERS_EXTENDED:
    str = ""
    for letter in BASE_LETTERS:
        str += f"{letter}{VIRAMA}{akhand} "
    ma_items.append({"item": str, "description": f"Virama {akhand} attachment"})

# show the same modifier on every consonant
for modifier in BASE_LETTER_MODIFIERS:
    str = ""
    for letter in BASE_LETTERS:
        str += f"{letter}{modifier} "
    ma_items.append({"item": str, "description": f"{modifier} attachment"})

# for every consonant, show each vowel, akhand, and other modifier as an attachment
for letter in BASE_LETTERS:
    str = ""
    for vowel in VOWEL_ATTACHMENTS:
        str += f"{letter}{vowel} "

    for akhand in BELOW_LETTERS + BELOW_LETTERS_EXTENDED:
        str += f"{letter}{VIRAMA}{akhand} "

    for modifier in BASE_LETTER_MODIFIERS + FINAL_MODIFIERS + [VISARGA]:
        str += f"{letter}{modifier} "

    ma_items.append({"item": str, "description": f"Mark attachments on {letter}"})
