# Sant Lipi Flex

An experimental font to see how far traditional gurmukhi can be expressed in modern forms for usage in digital media alongside latin fonts. Not meant for production use in Shabad OS.

## Aims/Goals

- Better fit gurmukhi alongside latin. Use metrics of something like Roboto Flex or Noto Sans (a font family which can cover multiple languages found in Shabad OS Database).
- Create more axes for font variations in addition to weight (thin/bold).
  - Re-use as many shapes/components as possible to make it easier to add axes.
  - Slant/Oblique (SLNT), which can be used to simulate an italic gurmukhi font.
  - Spacing (SPAC) for letter tracking.
  - Width (WDTH) with other custom ones like height, x-height, and accent distance.
  - Custom shirorekha/headline stroke height.
  - Roundness (ROND), to set up round corners/terminations
  - Monospace (MONO), which may lead to better gurmukhi rendering for programmers/terminals.
  - Morph (MORF) to simulate writing strokes of letters, this can be used as an animation.
  - Potentially many more such as Sharpness (SHRP) vs Softness (SOFT), proper Italics (ITAL), flare (FLAR)
- Use shirorekha/headline as a line to connect characters. Remove excess from initial / final positions.
- Use simple shapes / lines. Remove/replace serifs. The font doesn't have to be the way you write it, as very rarely do people write their latin letters as perfectly as they're expressed in typical fonts either.
- Document and solve combos that look similar to each other. For example ਗ। vs ਰ॥ (ਗ + । vs ਰ + ॥).

## Style

- Modern take on Gurmukhi glyphs. Historically written serif fonts migrated to straighter lines/simple curves to better render onscreen, so will this font align more with digital fonts today.
  - Strong focus on horizontal/vertical lines. Changing direction should be done with curves terminating/joining in horizontal/vertical directions. Avoid / remove all diagonal lines (often found in other gurmukhi fonts for ਅ, ਕ, ਣ, ੲ).
  - Removing traces of calligraphy from using italic nibs (no finials).
  - Replacing curved ball joints (such as on ਦ and ਚ, in the middle of ਅ and ਘ, and at the bottom-left of ੨).
  - Replacing left-hand stylistic curves for straight lines (such as left hand side of ਸ and ਪ).
  - Proper half-form glyphs (such as ੍ਯ) that connect with preceding character.
- Try to make main vertical stem of glyph be vertically connected to headline (no angled joins)
- Try to make bottom right vertical stem straight down or sub-join on a bottom descender curve/horizontal arm. This means ਕ, ਨ, and ਲ must have vertical stems at the bottom right. This leads to mostly vertically joined subletters with a potential variation for ਙ.
- Try to fit glyphs in aspect ratio categories around 1024 + 256 \* n (e.g. near 1024, 1280, 1536, ...) where n = 0 to 4.
  - Glyphs should go between a width-to-height ratio of 1:2 to 1:1.
  - No glyph should be wider than it is tall.
  - Try to fit 95% of glyphs between 1280 and 1800 width (n = 1 to 3)
  - All numerals (੦, ੧, ੨, ... ੭, ੮, ੯) must be same width.
- Open apertures (horizontally terminated) for heavier glyphs (e.g. ੲ and ਦ) and closed apertures (vertically terminated) for lighter glyphs (e.g. ਤ and ਹ). So it should be intuitive that ਭ is open and ੜ is closed.
- At font-weight 400, should fit the following at a line height of 1.35:
  - Low-point of double-u matra vs High-point of ik-oankar.
  - Low-point of pair-rara with double-u matra vs High-point of all upper vowel mark attachments with bindi / tippi / addak.
- All nuktas should be placed with their center at "baseline" metric.

## Experiments

- Smaller-width chars with sihari/bihari attached such that the compound fits closer to non-attached char space, which might make each "segment" of a word more visible. (It also solves a monospace issue, as you cannot have these vowel characters unattached).
- Remove headline inside the sihari/bihari to make it more of a seamless add-on to the character it's attached to.
- Narrow above-vowels has generally worked well for mid-stem. However for ਙ,the single left-stem char, try reverse above-vowels.

### Categories

**Subjoiner Shape**

- Vertical stem on right hand side (right-joined): ਅ, ਕ, ਖ, ਗ, ਘ, ਜ, ਥ, ਧ, **ਨ**, ਪ, ਬ, ਮ, ਯ, **ਲ**, ਸ
- Open-aperture; Horizontal arm on bottom (right-joined): ਞ, ਦ, ਣ, ਭ, ਵ, ੲ
- Horizontal arm into spiral counter (center-joined): ਢ, ਡ, ਫ
- Bottom descender curve (center-joined): ਚ, ਠ, ਤ, ਰ, ਹ, ੳ
- Uncategorized:
  - ਛ = should be horizontal bottom
  - ਟ = should be bottom descender curve (might end up horizontal bottom)

Other:

- ਙ and ਝ = off-position vertical stem in descender area
- ੜ = angled subjoiner. If we must have an angled-subjoiner variant, then perhaps ਨ and ਲ could also terminate at the appropriate angle for these subjoined variants. The only real use-case for ੜ is ੜ + ਹ = ੜ੍ਹ.

## Glyph Transforms

A great number of gurmukhi glyphs can be approximately represented by the latin letters H and U. The glyphs are being modified from Roboto Flex, an open-source font by Google.

---

- H
- ਮ = Shorten left stem from bottom
- ਸ = Then add headline

---

- H
- ਜ = Add headline and open top-left counter

---

- ਪ = U
- ਧ = Add headline
- ਥ = Then add horizontal bar
- ਖ = Remove headline

---

- ਪ = U
- ਹ = Shorten left stem
- ਚ = Then add horizontal bar
- ਦ = Open right-side counter

---

- ਪ = U
- ਘ = Double and modify center stem

---

- ਯ = U + H, then raise the entire curve of U (should match height of ਗ's curve)

---

Gurmukhi glyphs based on Latin glyph 3 or B:

- 3
- ਤ = Convert upper counter intersecting with headline into a vertical stem.
- ਡ = Close bottom counter spirally inwards.
- ਭ = Add an oval counter between two open counters. (Used part of ampersand as example for oval counter).
- ਕ = Convert bottom counter into an extended vertical bar on righthand side.

- ਤ
- ੳ = Add vertical bar on lefthand side. Add a closed counter above headline.
- ੲ = Flip horizontally, add vertical bar to close upper counter, open bottom counter with a horizontal termination.

- B
- ਬ = Flip horizontally, change connections at headline into vertical stems.

---

- d
- ਰ = Add headline.
- ਗ = Raise glyph by shortening vertical stem, then add vertical stem on right-hand side. Potentially curve the two vertical stems together at the headline to further differentiate this glyph from ਰ + । (danda).

---

- o
- ਠ = Add headline and centrally connect with vertical stem.
- ਟ = Move vertical stem to right-hand side, then open right counter.
- ਫ = Close counter in a spiral.
- ਙ = Flip horizontally and extend spiral counter.
- ਝ = ਙ with vertical stem replaced with a u-curve.

---

- ਠ = See above.
- ਨ = Open bottom counter.

---

- s
- ਛ = Terminate top-right as horizontal and add vertical stem. Close bottom counter and slash with vertical stem.

- s (or ε ?)
- ਵ = Join two rotated U shapes using the same metrics for the top, middle, and bottom sections of "s".
- ਞ = ਵ = Replace vertical stem with bottom u curve.

---

Unique shapes:

- ਅ = 3 Vertical Stems of H with a bottom quarter curve of a U joining initial bars and Horizontal Stem of H joining final bars.

## Shared Components / Similar Metrics

- H-Based: ਸ, ਮ, ਜ
- U-Based: ਪ, ਧ, ਖ, ਥ, ਨ, ਹ, ਚ

- CO-Based: ਟ, ਠ, ਣ, ਰ, ਢ, ਫ
- B3-Based: ਤ, ੜ, ਭ, ਵ, ੲ, ੳ, ਕ, ਦ
- Wide: ਅ
- Wider: ਗ, ਘ, ਯ,
- HU-Vertically-Stacked:

## Version 2 Process

### hun-based (11)

Two main styles ਪ and ਹ are based on lowercase "u" or "n"

- ਪ is metrically and shaped off lowercase "u"
- ਹ is the left portion of "u" mirrored
- Now have components to create ਪ, ਧ, ਖ, ਥ and also ਹ, ਚ, ਨ, ਲ
- These 7 chars all share the same metrics (e.g. 1138 width)

In Roboto Flex, h and n have same metrics width wise

- ਮ is metrically the same width as lowercase "h"
- Now have components to create ਸ, ਮ, ਜ

### B3-based (7)

An issue with 3 is for characters like ਤ, ੜ, ਭ, and ਦ which need to have an open/free terminal. The vertically ending terminal of the bottom counter creates issues with characters like ਦ, which ends up having very little to differentiate from ਚ. Characters like "e" and "g" often have open/free terminal angles.

Another issue is for differentiating ਦ and ੲ. It is important to use a horizontally-mirrored ਤ for ੲ for clarity. Cannot go too modern and make left-hand of ੲ a simple vertical stroke.

Use these bases for ਢ as well

### co-based (3)

- Use c for ਟ
- ਟ for ਣ with a curve at the intersection instead (using left-half of lowercase u)
- ਟ for ਫ and then ਙ as well

- Use o for ਠ

### m-based (1)

- Mirror both vertically and horizontally, then add vertical stems
- ਘ (e.g. 1764 width)

### special cases

- Use metrics of lowercase w for ਯ, but then use ਹ and horizontal/vertical stems to assemble.
- Use metrics of uppercase N for ਅ (sometimes looks better to use metrics of ਗ)

### Vowels

- Use À for laav
- Use metrics of Ã for hora
- Use ° (degree symbol) for tippi
- Use height of Ă and size of ă for addhak
- Use the bottom counter of "g" for aunkar (mirrored for symmetry)
- Use "engtail" found on Ŋ and ŋ for yakash
- Use ̛ combining horn U+031B found on Ơ ơ Ư ư for udaat and part of pair-haha
- Use modified size/angles of combining horn and À for pair-rara
- Use ˙ for nukta, bindi, period, etc.

### Numerals

Numerals should match metrically in width with each other (for tabular design in spreadsheets)

- Use 0 for ੦
- Use 9 for ੧
- Use R for ੨
- Use 3 for ੩
- Use 8 (open top counter into two vertical stems) for ੪
- Modified ਪ for ੫
- Reverse 3 and add numerical hook (U+031B rotate 180 degrees and left-extended) for ੬
- Bottom of e/g (used for B3-based characters like ਤ and ਦ) with angled line matching angle (but not terminating position) of 7 for ੭
- Add a horizontal stem to either bottom path of 3 component or mirrored-J for ੮
- Add numerical hook to ੮ for ੯
