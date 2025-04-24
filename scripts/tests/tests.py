import scripts.constants as constants
from scripts.tests.mark_attachments import ma_items
from scripts.tests.multi_vowel_attachments import mva_items
from scripts.tests.most_common_words import extra_fields_items
from scripts.tests.most_common_words import data_items

# Instantiate Tests
tests = []

gurmukhi_numerals = {0: "੦", 1: "੧", 2: "੨", 3: "੩", 4: "੪", 5: "੫", 6: "੬", 7: "੭", 8: "੮", 9: "੯"}


def number_to_gurmukhi(number):
    return "".join(gurmukhi_numerals[int(digit)] for digit in str(number))


def add_test(url, template, hash):
    tests.append({"url": url, "template": template, "hash": hash})


def add_side_by_side_test(url, title, items):
    hash = {
        "title": title,
        "items": items,
    }
    add_test(url, "side_by_side", hash)


def add_proof_sheet_test(url, title, items):
    hash = {
        "title": title,
        "items": items,
    }
    add_test(url, "proof", hash)


def dec2uni(decimal):
    return f"{format(ord(chr(decimal)), '04x')}"


items = [
    {"item": "ਙੰਙੇ ਘੰਙੇ", "description": "ਙੇ (6)"},
    {"item": "ਙੰਙੈ ਘੰਙੈ ਰੰਙੈ ਅੰਙੈ", "description": "ਙੈ (12)"},
    {"item": "ਆਪਣੇ ਸੋਹਣੇ ਗਹਿਣੇ ਨਿਮਾਣੇ ਡਰਾਉਣੇ ਲੈਣੇ ਛੈਣੇ ਛੈਂਣੇ ਹੀਣੇ ਜਾਂਣੇ", "description": "ਣੇ (28.8k)"},
    {"item": "ਜਾਣੈ ਭਾਣੈ ਪਛਾਣੈ ਵਖਾਣੈ ਆਣੈ ਪਤੀਣੈ ਆਪੀਣੈ ਜਿਣੈ ਦੇਣੈ ਲੈਣੈ ਨਾਰਾਇਣੈ ਪਉਣੈ", "description": "ਣੈ (1.8k)"},
    {"item": "ਝੂਠੇ ਬੈਠੇ ਇਕੱਠੇ ਅੱਠੇ ਮਿੱਠੇ ਉਠੇ ਮੀਠੇ ਕੋਠੇ ਕੱਠੇ ਕੰਠੇ ਪੁੱਠੇ ਉੱਠੇ ਠੇਂਗਾ ਡਿੱਠੇ", "description": "ਠੇ (2.5k)"},
    {"item": "ਉਠੈ ਡਿਠੈ ਮਜੀਠੈ ਕੈਠੈ ਉਠੈਂ ਬੈਕੁੰਠੈ ਉੱਠੈ ਮੁੱਠੈ ਐਂਠੈ", "description": "ਠੈ (੩੭੨)"},
    {"item": "ਨੇ ਅਪਨੇ ਕਰਨੇ ਅਨੇਕਾਂ ਅਨੇਕ ਨੇੜੇ ਖ਼ਜ਼ਾਨੇ ਤੈਨੇ ਜਿਤਨੇ ਕਿਤਨੇ ਮੈਨੇ ਮੈਂਨੇ ਹਨੇਰਾ ਨੇਤ੍ਰ ਮਹੀਨੇ ਨੇਤ੍ਰੋਂ ਹੋਨੇ ਮੰਨੇ ਤਿੰਨੇ ਜਿੰਨੇ ਤੈਂਨੇ ਓਨੇ ਉਨੇ ਉੱਨੇ", "description": "ਨੇ (67.9k)"},
    {"item": "ਨੈਨ ਜਾਨੈ ਮਾਨੈ ਚੀਨੈ ਮੰਨੈ ਨੈਣੰ ਇਨੈ ਪੰਨੈ ਨੈਂ ਨੈਨੋਂ ਨੈਨੌ ਉਨੈ", "description": "ਨੈ (3.7k)"},
    {"item": "ਸੰਙਿਆ ਙਿੱਕੀ", "description": "ਙਿ"},
    {"item": "ਬਾਣੀ ਵਰਨੀ ਸਿਰਠੀ", "description": "center bihari"},
]
add_proof_sheet_test("unsorted", "Unsorted", items)

BASE_CHARACTERS = (
    list(constants.VOWEL_LETTERS)
    + list(constants.BASE_LETTERS)
    + constants.YAYYA_LETTERS
    + constants.HALF_LETTERS
    + constants.MAHAN_KOSH_LETTERS
)

items = []
for letter in BASE_CHARACTERS:
    items.append({"item": f"{letter}\u0a02 {letter}\u0a70", "description": ""})
add_proof_sheet_test("anchor-nasal", "Anchor - Nasal", items)

items = []
for letter in BASE_CHARACTERS:
    items.append({"item": f"{letter}\u0a71{letter} {letter}\u0a01{letter}", "description": ""})
add_proof_sheet_test("anchor-gem", "Anchor - Gem", items)

items = []
for letter in BASE_CHARACTERS:
    items.append({"item": f"{letter}\u0a3c", "description": ""})
add_proof_sheet_test("anchor-nukta", "Anchor - Nukta", items)

items = []
for letter in BASE_CHARACTERS:
    appendage = ""
    for char in constants.BELOW_LETTERS + constants.BELOW_LETTERS_EXTENDED:
        appendage += f"{letter}{constants.VIRAMA}{char} "
    for mark in constants.VIRAMA + "ੑ" + "ੵ":
        appendage += f"{letter}{mark} "
    items.append({"item": f"{appendage.strip()}", "description": ""})
add_proof_sheet_test("anchor-joint", "Anchor - Joint", items)

items = []
for letter in BASE_CHARACTERS:
    appendage = ""
    for vowel in constants.TOP_VOWEL_ATTACHMENTS:
        appendage += f"{letter}{vowel} "
    items.append({"item": f"{appendage.strip()}", "description": ""})
add_proof_sheet_test("anchor-above-vowel", "Anchor - Above Vowel", items)

items = []
for letter in BASE_CHARACTERS:
    appendage = ""
    for vowel in constants.BOTTOM_VOWEL_ATTACHMENTS:
        appendage += f"{letter}{vowel} "
    items.append({"item": f"{appendage.strip()}", "description": ""})
add_proof_sheet_test("anchor-below-vowel", "Anchor - Below Vowel", items)

items = [
    {"item": f"ਨੀਂ{constants.NL['vs1']}ਦ", "description": "6"},
    {"item": f"ਤੁਹੀਂ{constants.NL['vs1']}", "description": "2"},
    {"item": f"ਗਲੀਂ{constants.NL['vs1']}", "description": "2"},
    {"item": f"ਕਰੀਂ{constants.NL['vs1']}", "description": "2"},
    {"item": f"ਕਿਤੀਂ{constants.NL['vs1']}", "description": "2"},
    {"item": f"ਨਕੀਂ{constants.NL['vs1']}", "description": "2"},
    {"item": f"ਵਢੀਂ{constants.NL['vs1']}", "description": "2"},
    {"item": f"ਅਖੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਕੁਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਮਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਵਡਭਾਗੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਗਣੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਸਿਫਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਰੂਪੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਮਾਲੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਹੀਂ{constants.NL['vs1']}ਅ", "description": "1"},
    {"item": f"ਮਨੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਸੀਂ{constants.NL['vs1']}ਗਾਰਾ", "description": "1"},
    {"item": f"ਕਾਲੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਕਤੇਬੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਸੀਂ{constants.NL['vs1']}ਗਾਰੁ", "description": "1"},
    {"item": f"ਬਡਭਾਗੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਅੰਧੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਹੀਂ{constants.NL['vs1']}ਉ", "description": "1"},
    {"item": f"ਨੀਂ{constants.NL['vs1']}ਦ੍ਰਾਵਲੇ", "description": "1"},
    {"item": f"ਥਿਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਲਿਖਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਸਗਲੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਸਉਦੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਰਾਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਜਾਂਹੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਭਾਵੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਗੁਣੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਭਗਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਮੀਂ{constants.NL['vs1']}ਰਾ", "description": "1"},
    {"item": f"ਥੁੜੀਂ{constants.NL['vs1']}ਦੋ", "description": "1"},
    {"item": f"ਕਚੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਨੀਂ{constants.NL['vs1']}ਵਾਂ", "description": "1"},
    {"item": f"ਚੰਦੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਦੁਨੀਂ{constants.NL['vs1']}ਆ", "description": "1"},
    {"item": f"ਸੀਂ{constants.NL['vs1']}ਗਾਰ", "description": "1"},
    {"item": f"ਗੁਰਸਿਖੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਧਰਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਸੁਰਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਸਲਾਹੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਸਖੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਰੂਖੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਬਿਰਖੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਮਖੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਬੁਧੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਪੁਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਗਨੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਬੇਦੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਨਾੜੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਭਤੀਜੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਸਨਾਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਰਾਗੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਵੇਦੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਸੀਂ{constants.NL['vs1']}ਗਾਰੋ", "description": "1"},
    {"item": f"ਦਾਤੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਥੀਂ{constants.NL['vs1']}ਧਾ", "description": "1"},
    {"item": f"ਨਥੀਂ{constants.NL['vs1']}", "description": "1"},
    {"item": f"ਧਰੀਂ{constants.NL['vs1']}", "description": "1"},
]
add_proof_sheet_test("db-bindi-before-bihari", "DB - Bindi Before Bihari", items)

# ASCII
items = []
for number in range(0, 128):
    items.append({"item": f"{chr(number)}", "description": dec2uni(number)})
add_side_by_side_test("ascii", "ASCII Range", items)

# Gurmukhi
# Gurmukhi block goes from U+0A00 to U+0A7F
# ord('\u0a00') = 2560
# ord('\u0a7f') = 2687
items = []
for number in range(2560, 2688):
    items.append({"item": f"{chr(number)}", "description": dec2uni(number)})
add_side_by_side_test("gurmukhi", "Gurmukhi Code Block", items)

# SPG
items = [
    {"item": "ਉਤ੍ਕਟ", "description": "small k"},
    {"item": "ਬ੍ਰਹ੍ਮ", "description": "half m"},
    {"item": "ਉਤਬ੍ਰਹਮਨੇਸ਼੍ਠੀਟ", "description": "small ṭ"},
    {"item": "ਧੵਾਨੰ", "description": "yakash"},
    {"item": "ਸ਼੍ਰੀ", "description": "compound letter + small rara"},
    {"item": "ਦੇਹਿ ਬਿਖੈ", "description": "mark attachments"},
    {"item": "ਉੱਤਰ", "description": "ura + addak"},
    {"item": "ਯੌਂ", "description": "ō + nasalization"},
    {"item": "ਪ੍ਰਫੁੱਲਤ", "description": ""},
    {"item": "ਜ੍ਯੋਂ", "description": ""},
    {"item": "ਨਿੰਦਾ", "description": "midstem sihari + nasal"},
    {"item": "ਸੁਨੈਂ", "description": "midstem dulav + nasal"},
    {"item": "ਸ਼੍ਰੁਤ", "description": ""},
    {"item": "ਗਹੈਂ", "description": "dulav + nasal"},
]
add_proof_sheet_test("spg", "SPG", items)

# Markup
items = [
    {"item": "\u0a28\u0a40\u0a02", "description": "Bindi After (ੀ + ਂ)"},
    {"item": "\u0a28\u0a02\u0a40 \u0a15\u0a1a\u0a02\u0a40", "description": "Bindi Before (ਂ + ੀ) Harfbuzz"},
    {
        "item": f"\u0a28\u0a02{constants.NL['zwj']}\u0a40 \u0a15\u0a1a\u0a02{constants.NL['zwj']}\u0a40",
        "description": "Bindi Before (ਂ + ZWJ + ੀ) Coretext",
    },
    {
        "item": f"\u0a28\u0a40\u0a02{constants.NL['vs1']} \u0a15\u0a1a\u0a40\u0a02{constants.NL['vs1']}",
        "description": "VS1 workaround for both",
    },
    {"item": "\u0a28\u0a40\u0a70", "description": "Tippi (ੀ + ੰ)"},
]
add_proof_sheet_test("bindi-tippi", "Bindi & Tippi", items)

# Yayya
items = [
    {"item": "ਯ", "description": "full yayya"},
    {"item": "ਯੈਂ", "description": "full yayya"},
    {"item": "ਯੂੰ", "description": "full yayya"},
    {"item": "ਯੌਂ", "description": "full yayya"},
    {"item": "ਯੀਂ", "description": "full yayya"},
    {"item": "ਯੂਜ਼ਿ", "description": "full yayya"},
    {"item": "ਯਾਰਿ", "description": "full yayya"},
    {"item": "ਹਯਾੱਤਿ", "description": "full yayya"},
    {"item": "ਪ੍ਰਿਯ", "description": "full yayya"},
    {"item": "ਹਮਾਯੂੰ", "description": "full yayya"},
    {"item": "ਭਯੋੁ", "description": "full yayya"},
    {"item": "ਯਕੀਨ", "description": "full yayya"},
    {"item": "︀ਯ", "description": "half yayya"},
    {"item": "︀ਯ", "description": "VS1 + half yayya"},
    {"item": "ਤ੍ਯ", "description": "half yayya"},
    {"item": "ਤ︀ਯੰ", "description": "half yayya, attachment on yayya"},
    {"item": "ਤ︀ਯਾ", "description": "half yayya, attachment on yayya"},
    {"item": "ਹ੍ਯਾਂ", "description": "half yayya, attachment on yayya"},
    {"item": "ਤ੍ਯਾਗਿ", "description": "half yayya, attachment on yayya"},
    {"item": "ਜ੍ਯੋਂ", "description": "half yayya, attachment on yayya"},
    {"item": "ਤ੍ਯੌਂ", "description": "half yayya, attachment on yayya"},
    {"item": "ਲ੍ਯੈਯੈ", "description": "half yayya, attachment on yayya"},
    {"item": "ਭਿ︀ਯੋ", "description": "half yayya, attachment on pre"},
    {"item": "ਭਿ੍ਯੋ", "description": "half yayya, attachment on pre"},
    {"item": "ਕੀ︀ਯੋ", "description": "half yayya, attachment on pre"},
    {"item": "ਕੀ੍ਯੋ", "description": "half yayya, attachment on pre"},
    {"item": "︁ਯ", "description": "open-top yayya"},
    {"item": "ਤ︁ਯਾ", "description": "open-top yayya"},
    {"item": "ਆ︁ਯੋ", "description": "open-top yayya"},
    {"item": "ਪਾ︁ਯਾ", "description": "open-top yayya"},
    {"item": "ਰਾ︁ਯੰ", "description": "open-top yayya"},
    {"item": "ਦੇ︁ਯੰ", "description": "open-top yayya"},
    {"item": "︀︁ਯ", "description": "open-top half yayya"},
    {"item": "ਤ︂︀︁ਯ", "description": "open-top half yayya"},
    {"item": "ਤ੍ਰਸ︂︀︁ਯੋ", "description": "open-top half yayya"},
]
add_proof_sheet_test("yayya", "Yayya", items)

# Mahan Kosh
items = [
    {"item": "︃ਸ", "description": "स् (half s) = VS4 + ਸ"},
    {
        "item": f'{constants.NL["sh"]}{constants.NL["kana"]}{constants.NL["s"]}{constants.NL["halant"]}{constants.NL["zwj"]}{constants.NL["t"]}{constants.NL["halant"]}{constants.NL["r"]}',
        "description": "ਸ + ੍ + ZWJ",
    },
    {"item": "︄ਧ", "description": "VS5 + ਧ"},
    {"item": "︄ਧ਼", "description": "ष (ṣ) = VS5 + ਧ਼"},
    {"item": "︃︄ਸ", "description": "ष् (half ṣ) and श् (half ś) = VS4 + VS5 + ਸ"},
    {"item": "︄ਕ", "description": "क्ष (kṣa) = VS5 + ਕ"},
    {"item": "︁︄ਕ", "description": "क्ष् (half kṣa) = VS2 + VS5 + ਕ"},
    {"item": "ਜ੍ਞ", "description": "ज्ञ (jña) = ਜ + ੍ (virama) + ਞ"},
    {"item": "੍ਮ", "description": "म् (half m) =  ੍ (virama) + ਮ"},
    {"item": "ਰ਼", "description": "ऋ (ṛ)"},
    {"item": "︅ਸ", "description": "ص (ṣâd) = VS6 + ਸ"},
    {"item": "︇ਸ", "description": "ث (s̱e) =  VS8 + ਸ"},
    {"item": "︅ਜ", "description": "ذ (ẕâl) = VS6 + ਜ"},
    {"item": "︆ਜ", "description": "ژ (že) = VS7 + ਜ"},
    {"item": "︇ਜ", "description": "ض (zâd) = VS8 + ਜ"},
    {"item": "︈ਜ", "description": "ظ (ẓâ) = VS9 + ਜ"},
    {"item": "ਖ਼", "description": "خ (xe)"},
    {"item": "ਜ਼", "description": "ز (ze)"},
    {"item": "ਤ਼", "description": "ط (tâ)"},
    {"item": "ੳ਼", "description": "ع (ʿayn)"},
    {"item": "ਅ਼", "description": "ع (ʿayn)"},
    {"item": "ੲ਼", "description": "ع (ʿayn)"},
    {"item": "ਗ਼", "description": "غ (ġayn)"},
    {"item": "ਫ਼", "description": "ف (fe)"},
    {"item": "ਕ਼", "description": "ق (qâf)"},
]
add_proof_sheet_test("mahan-kosh", "Mahan Kosh", items)

# Subscript Numerals
items = [
    {"item": "ਮਾਝ₁ਮਾਝ₁", "description": "Subscript 1"},
    {"item": "ਬੈਰਾਗਣਿ₁ਬੈਰਾਗਣਿ₁", "description": "Subscript 1"},
    {"item": "ਤਿਪਦੇ₁₅ਤਿਪਦੇ₁₅", "description": "Subscript 1 & 5"},
    {"item": "ਮਾਲਾ₂", "description": "Subscript 2"},
    {"item": "ਕਾਫੀ₂", "description": "Subscript 2"},
    {"item": "ਚਾਰਤੁਕੇ₂", "description": "Subscript 2"},
    {"item": "ਪੰਚਪਦੇ₂", "description": "Subscript 2"},
    {"item": "ਦੁਪਦੇ₂", "description": "Subscript 2"},
    {"item": "ਤਿਪਦੇ₃", "description": "Subscript 3"},
    {"item": "ਚਉਪਦੇ₄", "description": "Subscript 4"},
    {"item": "ਪੂਰਬੀ₄", "description": "Subscript 4"},
    {"item": "ਗਉੜੀ₅", "description": "Subscript 5"},
    {"item": "ਪੰਚਪਦੇ₆", "description": "Subscript 6"},
    {"item": "ਗਉੜੀ₈", "description": "Subscript 8"},
    {"item": "ਟੈਸਟ₇", "description": "Subscript 7"},
    {"item": "ਟੈਸਟ₉", "description": "Subscript 9"},
    {"item": "ਟੈਸਟ₀", "description": "Subscript 0"},
]
add_proof_sheet_test("subnum", "Subscript Numerals", items)

# Diacritics
items = [
    {"item": "ਕ੍ਰਾਂ", "description": ""},
    {"item": "ਸ੍ਵਾਂ", "description": ""},
    {"item": "ਨ੍ਰਿੱ", "description": ""},
    {"item": "ਨੵਿੰ", "description": ""},
    {"item": "ਮ੍ਰਿੱ", "description": ""},
    {"item": "ਭ੍ਰਿੰ", "description": ""},
    {"item": "ਕ੍ਰੁੱ", "description": ""},
    {"item": "ਨ੍ਹੈਂ", "description": ""},
    {"item": "ਹ੍ਵੈੁ", "description": ""},
    {"item": "ਖ਼ੁੱਦ", "description": ""},
    {"item": "ਖ਼ੁੱਰੋ", "description": ""},
    {"item": "ਨੑੁ", "description": ""},
    {"item": "ਹੁਂ", "description": ""},
    {"item": "ਦੇਂ", "description": ""},
    {"item": "ਤੀੰ", "description": ""},
    {"item": "ਕੀੰ", "description": ""},
    {"item": "ਨੀੰ", "description": ""},
    {"item": "\u0a28\u0a40\u0a70", "description": ""},
    {"item": "ਧ੍ਰੂ", "description": ""},
    {"item": "ਸ੍ਯ", "description": ""},
    {"item": "ਸ੍ਟ", "description": ""},
    {"item": "ਸ੍ਨੰ", "description": ""},
    {"item": "ਸ੍ਤ", "description": ""},
    {"item": "ਸ੍ਚ", "description": ""},
    {"item": "ਸ੍ਵਾ", "description": ""},
    {"item": "ਖੵ", "description": ""},
    {"item": "ੜ੍ਹੂ", "description": ""},
    {"item": "ਮੵਿਾ", "description": ""},
    {"item": "ਧੵਿਾ", "description": ""},
    {"item": "ਥੵੰਤ", "description": ""},
    {"item": "\u0a32\u0a75\u0a3f\u0a4b", "description": ""},
    {"item": "ਮ੍ਰਿਤੵੁ", "description": ""},
]
add_proof_sheet_test("diacritics", "Diacritics", items)

items = []
add_to_loop = ["ਿ", "ਿੰ", "ਿੱ"]
for adder in add_to_loop:
    string = ""
    for letter in constants.BASE_LETTERS:
        string += f"{letter}{adder} "
    items.append(
        {"item": string, "description": adder},
    )
add_proof_sheet_test("sihari-combos", "Sihari Combos ਿ", items)

items = ma_items
add_proof_sheet_test("mark-attachments", "Mark Attachments", items)

items = mva_items
add_proof_sheet_test("multi-vowel-attachments", "Multiple Vowel Attachments", items)

items = data_items
add_proof_sheet_test("common-words-data", "Common Words in Src", items)

items = extra_fields_items
add_proof_sheet_test("common-words-extra-fields", "Common Words in Extra Fields", items)

items = [
    {"item": "ਦੇਂਹਿ", "description": "Bindi between vowels"},
    {"item": "ਹੋਂਹਿ", "description": "Bindi between vowels"},
    {"item": "ਰੋਂਦੇ", "description": "Bindi between vowels"},
    {"item": "ਲੈਂਦਿਆਂ", "description": "Bindi between vowels"},
    {"item": "ਸਾਂਤਿ", "description": "Bindi between vowels"},
    {"item": "ਐਂਠੈ", "description": "Bindi between vowels"},
    {"item": "ਐਂਠੇ", "description": "Bindi between vowels"},
    {"item": "ਭੰਨੇ", "description": "Tippi + pre/above attachment"},
    {"item": "ਅੰਤਿ", "description": "Tippi + pre/above attachment"},
    {"item": "ਅੰਮ੍ਰਿਤਸਰ", "description": "Tippi + pre/above attachment"},
    {"item": "ਙੰਙੈ", "description": "Tippi + pre/above attachment"},
    {"item": "ਅੰਙੈ", "description": "Tippi + pre/above attachment"},
    {"item": "ਰੰਙੈ", "description": "Tippi + pre/above attachment"},
    {"item": "ਕਿੰਨੇ", "description": "Tippi + pre/above attachment"},
    {"item": "ਮੁੰਨੇ", "description": "Tippi + pre/above attachment"},
    {"item": "ਮੰਨੈ", "description": "Tippi + pre/above attachment"},
]
add_proof_sheet_test("db-words", "DB Words", items)


items = [
    {
        "item": "",
        "description": "theory that a few numbers come from the same letter as they are described with. notables include 1, 2, 3, 4, 5, 6. see also evolution of numbers: Georges Ifrah, The Universal History of Numbers pp 368-396.",
    },
    {"item": "੧ੲ੧ੲ", "description": "੧ ਇੱਕ"},
    {"item": "੨ਦ੨ਦ", "description": "੨ ਦੋ"},
    {"item": "੩ਤ੩ਤ", "description": "੩ ਤਿੰਨ"},
    {"item": "੪ਚ੪ਚ", "description": "੪ ਚਾਰ"},
    {"item": "੫ਪ੫ਪ", "description": "੫ ਪੰਜ"},
    {"item": "੬ਛ੬ਛ", "description": "੬ ਛੇ"},
    {"item": "੭ਸ੭ਸ", "description": "੭ ਸੱਤ"},
    {"item": "੮ਅ੮ਅ", "description": "੮ ਅੱਠ"},
    {"item": "੯ਨ੯ਨ", "description": "੯ ਨੌਂ"},
]
add_proof_sheet_test("letter-numbers", "Letter-Number Comparison", items)

items = []
for number in range(0, 1000):
    items.append({"item": number_to_gurmukhi(number), "description": ""})
add_proof_sheet_test("1000numbers", "Numbers 0-1000", items)

items = [{"item": "ਲੰ", "description": ""}]
add_side_by_side_test("nasal-attachment", "Nasalizations", items)

items = [
    {"item": f'{constants.NL["ikoankar"]} {constants.NL["s"]}{constants.NL["t"]}{constants.NL["sihari"]}', "description": ""},
    {"item": "ਮੰਨੈ", "description": ""},
    {"item": "ਤੁਧਨੋ", "description": ""},
    {"item": "ਤ੍ਵ ਪ੍ਰਸਾਦਿ", "description": ""},
]
add_proof_sheet_test("words-from-nitnem", "Words From Nitnem", items)

items = [
    {"item": "ਆਦਿ ਸਚੁ\ue000", "description": ""},
]
add_proof_sheet_test("vishram", "Vishram Symbols", items)

items = [
    {"item": "ਭਾਉ॥ਮਸੂ", "description": "without spaces"},
    {"item": "ਭਾਉ॥ ਮਸੂ", "description": "spaced"},
    {"item": "ਭਾਉ ॥ ਮਸੂ", "description": "spaced"},
    {"item": "ਨਾਉ॥੪॥੨॥", "description": "without spaces"},
    {"item": "ਨਾਉ॥੪॥੨॥", "description": "spaced"},
    {"item": "ਨਾਉ ॥੪॥੨॥", "description": "spaced"},
    {"item": "ਨਾਉ ॥ ੪॥੨॥", "description": "spaced"},
    {"item": "ਨਾਉ ॥ ੪ ॥੨॥", "description": "spaced"},
    {"item": "ਨਾਉ ॥ ੪ ॥ ੨॥", "description": "spaced"},
    {"item": "ਨਾਉ ॥ ੪ ॥ ੨ ॥", "description": "spaced"},
    {"item": "ਨਾਉ॥੪॥੨॥ਸਿਰੀਰਾਗੁਮਹਲਾ੧॥ਲੇਖੈ", "description": "without spaces"},
    {"item": "ਨਾਉ ॥੪॥੨॥ ਸਿਰੀਰਾਗੁ ਮਹਲਾ ੧ ॥ ਲੇਖੈ", "description": "spaced"},
    {"item": "ਓਹੁ॥੧॥ਰਹਾਉ॥ਜੀਵਣ", "description": "without spaces"},
    {"item": "ਓਹੁ ॥੧॥ ਰਹਾਉ ॥ ਜੀਵਣ", "description": "spaced"},
    {"item": "ਭਾਗ॥ਆਦੇਸੁ", "description": "without spaces"},
    {"item": "ਭਾਗ ॥ ਆਦੇਸੁ", "description": "spaced"},
    {"item": "ਵਾਰ॥ਚੁਪੈ", "description": "without spaces"},
    {"item": "ਵਾਰ ॥ ਚੁਪੈ", "description": "spaced"},
    {"item": 'ੴਸਤਿ ੴਸ੍ਰੀ ੴਵਾਹਿ ੴਹੁਕਮ (ੴ) "ੴ" ੴ 13', "description": "ੴ without spaces"},
    {"item": 'ੴ ਸਤਿ ੴ ਸ੍ਰੀ ੴ ਵਾਹਿ ੴ ਹੁਕਮ ( ੴ ) " ੴ " ੴ 13', "description": "ੴ spaced"},
]
add_proof_sheet_test("doubledanda", "Double ਡੰਡਾ/ਹੱਦ character (॥)  #53", items)
