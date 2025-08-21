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
  - Replacing curved ball joints (such as on ਦ and ਚ, in the middle of ਅ and ਘ, and at the bottom of ੨).
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

- ਤ
- ਡ = Close bottom counter spirally inwards.
- ਭ = Add an oval counter between two open counters.
- ਬ
- ੳ
- ੲ

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

- o
- ਛ = Add headline, vertical

---

Unique shapes:

- ਅ = 3 Vertical Stems of H with a bottom quarter curve of a U joining initial bars and Horizontal Stem of H joining final bars.
- ਵ = ε = Add headline and connect with vertical stem.
- ਞ = ਵ = Replace vertical stem with bottom u curve.
