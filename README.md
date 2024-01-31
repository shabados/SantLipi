# Sant Lipi

A [unicode](<https://en.wikipedia.org/wiki/Gurmukhi_(Unicode_block)>) font for extraordinary [Gurmukhi](https://en.wikipedia.org/wiki/Gurmukhi).

Sant Lipi is associated with the phrase Sant Bhasha and the word _lipi_. [Sant Bhasha](https://en.wikipedia.org/wiki/Sant_Bhasha) refers to the vocabulary and languages contained within [Sri Guru Granth Sahib Ji](https://en.wikipedia.org/wiki/Guru_Granth_Sahib). The word [_lipi_](https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%BF%E0%A4%AA%E0%A5%80) means script or writing.

The font is packaged for [GitHub](https://github.com/shabados/SantLipi/releases) and [npm](https://www.npmjs.com/package/sant-lipi). QA for the latest font version is available on [GitHub Pages](https://shabados.github.io/SantLipi).

## About

The [Shabad OS Database](https://github.com/shabados/database) aims to faithfully represent the historicity of Gurbani and other Sikh Bani. Some portions contain atypical usage of modern-day Gurmukhi (e.g. tippi in place of bindi, unused yayya variations). In the past, ASCII fonts were used to render custom Gurmukhi (e.g. [Open Gurbani Akhar](https://github.com/GurbaniNow/gurmukhi-fonts)). As far as I knew, no such Unicode font existed to replace these ASCII fonts, so Sant Lipi was created.

Sant Lipi uses ligatures with specific markup characters. These characters or combos are unlikely to be accepted by the [Unicode Consortium](https://en.wikipedia.org/wiki/Unicode_Consortium), as they go against modern-day usage. Plenty examples exist of proposals asking for these characters to be added (e.g. [L2/20-076](https://www.unicode.org/L2/L2020/20076-gurmukhi-sum.pdf), [L2/20-183](https://www.unicode.org/L2/L2020/20183-gurmukhi-chg.pdf), etc.). So resorting to using markup to preserve Gurbani through Unicode seems to be the best option for now.

Note that Sant Lipi is a modification of [Mukta Mahee](https://github.com/EkType/Mukta) by [Ek Type](https://ektype.in/). As of writing, Mukta Mahee was the default Unicode font for Gurmukhi on Apple programs (i.e. iOS, iPad OS, macOS, Safari, etc.). Adding custom glyphs and ligatures is enough to faithfully represent all of the Gurmukhi in the Shabad OS Database.

The reason Shabad OS is committing to switch from ASCII to Unicode is simple. Over 99% of Shabad OS Database lines are faithfully represented using current Unicode standards. Percentage of all word instances increases very close to 100%. With Unicode, we will be able to better proofread the data directly. With Sant Lipi as our standard we also create stronger cohesion with our [Gurmukhi Utils](https://github.com/shabados/gurmukhi-utils) projects.

Sant Lipi is created using [Glyphs 3](https://glyphsapp.com/).

## Using Packages

**npm** - See [`packages/npm`](packages/npm/sant-lipi/README.md) or view the package on [npmjs.com](https://www.npmjs.com/package/sant-lipi). This has been used successfully on various frameworks including Next.js, Preact, React, Svelte, and Vue.

**Dart and Flutter apps** - See [`packages/pubdev`](packages/pubdev/sant_lipi/README.md) or view the package on [pub.dev](https://pub.dev/packages/sant_lipi).

## Manual Usage

Work with the font files by downloading and extracting the zip file from the [latest release](https://github.com/shabados/SantLipi/releases/latest) on GitHub.

**Desktop** - Select all files in the `ttf` folder, right-click, and either "Install for all users" (Windows) or "Open with Font Book/Viewer" (macOS/Linux). It is recommended to uninstall any previous versions of Sant Lipi before installing a new version.

**CSS** - WOFF2 is the same as TTF but compressed for lower bandwidth usage. A variable font is a new font specification that significantly reduces font file sizes. All modern browsers support WOFF2 and variable fonts. See how the Test Suite defines the variable font in [`build/qa/style.css`](build/qa/style.css). Learn more about WOFF2 [here](https://web.dev/font-best-practices/#use-woff2). Learn more about variable fonts [here](https://web.dev/variable-fonts). Sant Lipi's font weight varies from 100 to 900.

**VS Code** - Sant Lipi can render Gurmukhi in [VS Code](https://code.visualstudio.com/) without affecting the source code. See the below example of user preferences/settings in VS Code.

```json
"editor.fontFamily": "Consolas, 'Sant Lipi', monospace",
```

## Ligature Combos / Markup Language

[Variation Selectors](<https://en.wikipedia.org/wiki/Variation_Selectors_(Unicode_block)>) are used to specify standardized variation sequences according to the Unicode Consortium. The Unicode Consortium dictates VS should only be applied to the immediately preceding character, and a character should have at most one VS following it. However, please note the difference between the Unicode Consortium and Sant Lipi conventions: (1) Sant Lipi uses some VS as preceding markup and (2) Sant Lipi allows for multiple VS to be used in sequence.

Note that in Sant Lipi a Sihari (ਿ) can be added to the typical full Yayya (ਯ), but the Yayya variants cannot render Sihari (ਿ) properly. As of yet, it's unknown if such a sequence is required.

**Open Side**

VS1-4 (`U+FE00` - `U+FE03`) opens the left, top, bottom, and right sides (respectively). For example:

- Half Yayya (੍ + ਯ), VS1 + ਯ
- Open-Top Yayya, VS2 + ਯ
- Open-Top Half Yayya, VS1 + VS2 + ਯ
- Open-Right Sassa, VS4 + ਸ

**Bihari Nasals**

- Tippi before Bihari, ੀ + ੰ
- Bindi before Bihari, ੀ + ਁ (`U+0A01`: Adak Bindi)

**Extra**

- Subscript Gurmukhi Numerals, ₀ ₁ ₂ ...

**Mahan Kosh**

VS5-9 (`U+FE04` - `U+FE08`) are used for special chars in Mahan Kosh. As tracked in [shabados/SantLipi#41](https://github.com/shabados/SantLipi/issues/41) ([PDF](https://user-images.githubusercontent.com/14130567/234413746-8965a06e-6eeb-4a11-9d2d-01c5213f17e2.png) and [Scan](https://user-images.githubusercontent.com/14130567/258670089-edd443ef-b28c-4a03-bc4c-21eca9d0153f.jpeg)).

- VS5 adds a slash/stroke to the following character's [counter](<https://en.wikipedia.org/wiki/Counter_(typography)>)
- VS6 attaches a dot above the crossbar
- VS7 attaches a dot below the crossbar
- VS8 daggers the crossbar
- VS9 adds a bar to the stem in the counter area

Devanagari:

- स् (half s) = VS4 + ਸ
- ष (ṣ) = VS5 + ਧ + ਼ (nukta)
- ष् (half ṣ) and श् (half ś) = VS4 + VS5 + ਸ
- क्ष (kṣa) = VS5 + ਕ
- क्ष् (half kṣa) = VS2 + VS5 + ਕ
- ज्ञ (jña) = ਜ + ੍ (virama) + ਞ
- म् (half m) = ੍ (virama) + ਮ
- ऋ (ṛ) = ਰ + ਼ (nukta)

Perso-Arabic:

- (ṣâd) ص = VS6 + ਸ
- (s̱e) ث = VS8 + ਸ
- (ẕâl) ذ = VS6 + ਜ
- (že) ژ = VS7 + ਜ
- (zâd) ض = VS8 + ਜ
- (ẓâ) ظ = VS9 + ਜ

Nuktas:

- (xe) خ = ਖ਼
- (ze) ز = ਜ਼
- (tâ) ط = ਤ਼
- (ʿayn) ع = ੳ਼ ਅ਼ ੲ਼
- (ġayn) غ = ਗ਼
- (fe) ف = ਫ਼
- (qâf) ق = ਕ਼

Not yet implemented:

- र् (half r). This is not pairin-rara in punjabi, which comes after the consonant, instead this is a half-r preceding the conjunct, even though it is written at the far top right of the conjunct, it is pronounced initially in the cluster.
- Addak Bindi. This exists in Gurmukhi unicode block already. However, in Sant Lipi it is specifically being used to produce a bindi before bihari. Probably will have to change that strategy (aside from Mahan Kosh, I have only seen it in obscure and niche old dictionaries).

## Quality Assurance

Sant Lipi has been tested using React Native's text component on Android and iOS, Chrome and Firefox on Windows and macOS, Edge on Windows, and Safari on macOS. Sant Lipi renders correctly via multiple text shaping engines including Uniscribe, CoreText, and HarfBuzz.

Unicode standards and text shaping engines will continue to improve. Yet, there have been key points in time during the past decade which have shaken Gurmukhi rendering. In an effort to combat that, the latest release can be tested online with our [Sant Lipi Test Suite](https://shabados.github.io/SantLipi).

If you wish to work offline and run QA locally, please see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Community

If you wish to provide assistance or contribute to the future of this project, please see [CONTRIBUTING.md](./CONTRIBUTING.md).

Bhajneet S.K. ([@bhajneet](https://github.com/bhajneet/)) is the author and lead maintainer of Sant Lipi.

_Special thanks_ to:

- [Ek Type](https://ektype.in/) for creating the original Mukta Mahee font (see [GitHub](https://github.com/EkType/Mukta)).

## Approach

Unicode consists of code points. The gurmukhi letters, accents, and punctuation we see on our screens are represented by these code points.

Gurmukhi is special in that there are various marks or symbols that can be added to the same base letter. Some occur above (e.g. hora ੋ or addak ੱ) and others occur below (e.g. pairi rara ੍ਰ or aunkar ੁ). The accents can appear in any order, but there is a preferred method.

There are different text shaping engines (e.g. Uniscribe/Universal Shaping Engine on Windows, CoreText on macOS, or HarfBuzz on any). The job of these is to render the text properly (e.g. ligatures and reordering).

So we might type the sihari ਿ after an iri ੲ, but we will see it re-ordered before as ਇ. Another example would be that we type a tippi ੰ after a bihari ਈ, but instead of seeing a tippi and bihari, the shaping engine renders a bindi (as according to today's grammar), meaning a ਈੰ.

Note that the code points do not change in the background. Even though you see the sihari before the iri ਇ, the code still remains ੲ+ਿ (or in Unicode 0A72+0A3F). Continuing the example, even if you see a bindi, the code still points to a tippi. The first example is of a reordering, the second is an example of a ligature.

For Indic scripts, the text should be applied in order (e.g. starting with nuktas, then akhand forms, then vowels, half forms / post-base forms, etc.). For more reading see the [OpenType Microsoft Docs](https://docs.microsoft.com/en-us/typography/opentype/spec/features_pt#pstf).

This can vary between different text shaping engines, but the general order (with a running example) for Gurmukhi diacritics is:

1. Base Letter (ਸ)
2. Nukta (ਸ਼ = ਸ+਼)
3. Akhand (ਸ਼੍ਰ = ਸ+਼+੍+ਰ)
4. Vowel (ਸ਼੍ਰੀ = ਸ+਼+੍+ਰ+ੀ)
5. Nasalizations, Addhak, or other Miscellaneous marks / symbols (ਸ਼੍ਰੀਃ = ਸ+਼+੍+ਰ+ੀ+ਃ)

The big problem is where half-forms / post-base forms are ordered. The most common example in Gurmukhi is half yayya / addha yayya (e.g. found at the end of ਆਗ੍ਯਾ).

In Unicode and every font shaping engine (as of writing), this is considered (quite unfortunately) as a post-base form of Yayya (ਯ). It is renderded using a subjoined letter combiner (i.e. using ੍+ਯ). That means it is intrinsically tied to the Base Letter from step 1 as if it were an Akhand like the one in step 3. So the same way you type the pairi rara ੍ਰ is how you get the half yayya base character.

Ultimately, this means that the half-yayya is intrinsically tied to the preceding base letter. So you cannot have separate vowels for the half-yayya and the preceding base letter. If post-base forms fit after Akhands but before Vowels (see above), then vowels will only be applied to the half-yayya. If you place post-base forms after Vowels, you break the shaping engines algorithms. It will assume you're trying to create a new base letter (which a half-yayya pretty much acts as it's own base letter, though never at the start of a word). Thus you'll end up with vowels on the preceding letter, a broken yayya symbol, and no vowels on what was supposed to be the half-yayya. While some words work in Chrome (e.g. ਭ੍ਯਿੋ), others break regardless ( ਕੀ੍ਯੋ should be using a half-Y). This is tied to the text shaping engines and how they interpret Indic syllables.

There are many workarounds Sant Lipi could have used, but ultimately everything is being done with OpenType Features, namely ligatures.

**Attempted Workarounds**

One idea was to use PUA code points. However these are ignored by text shaping engines. If there is a half-Y with a Bihari ੀ or Kanna ਾ attached to it, line-breaks will mess up and send the vowel to the next line while leaving the half-Y on the preceding line. So then unique code points for all vowel variations would be required for the PUA approach. Not a good idea for maintainability.

Another idea was to use discretionary font features, such as historical ligatures or styled sets. Basically to take the codepoint of a Yayya (ਯ) and change it to a half yayya or open-top yayya with discretionary ligatures. But this requires specifically changing a substring's discretionary ligatures. So it would still require markup in the database to signify which substrings to affect. In addition, font features such as these are poorly supported in VS Code, React Native, etc. So this approach would not work for Shabad OS apps.

**Current Workaround**

Currently, the approach taken by Sant Lipi is to use markup to indicate Yayya variations. It is similar to how a Half Yayya is constructed in today's practice (੍+ਯ). So to show an open-top Yayya, one can type VS2 + ਯ (`U+FE01`: Variation Selector-1 + `U+0A2F`: Yayya). Let's walk through really quickly what is happening in the background:

- `ltra` - First, the earliest font features are being applied by replacing codepoints for later font features to act upon.
- `rlig` - Then, render Yayya (ਯ) according to any markup preceding it

The `ltra` is for making the earliest substitutions possible. This replaces the Virama ੍ (subjoined letter combiner) before text shaping engines look at it. Notably, this is what allows vowels and marks on both the Half Yayya and the letter preceding it (aside from Sihari on Yayya variants).

After this step, ligatures are used to render combos of Yayyas as if they were different variations.
