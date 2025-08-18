# Sant Lipi Flex

An experimental font.

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

### Glyph Transforms

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

- ਯ = U + H

---

Gurmukhi glyphs based on Latin glyph 3 or B:

- ਤ
- ਬ
- ੳ

---

- ਅ = 3 Vertical Stems of H with a bottom quarter curve of a U joining initial bars and Horizontal Stem of H joining final bars.
- ਰ = The letter d with added headline.
