# Sant Lipi

A [unicode](<https://en.wikipedia.org/wiki/Gurmukhi_(Unicode_block)>) font for extraordinary [Gurmukhi](https://en.wikipedia.org/wiki/Gurmukhi).

Sant Lipi is associated with the phrase Sant Bhasha and the word _lipi_. [Sant Bhasha](https://en.wikipedia.org/wiki/Sant_Bhasha) refers to the vocabulary and languages contained within [Sri Guru Granth Sahib Ji](https://en.wikipedia.org/wiki/Guru_Granth_Sahib). The word [_lipi_](https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%BF%E0%A4%AA%E0%A5%80) means script or writing.

## About

The [Shabad OS Database](https://github.com/shabados/database) aims to faithfully represent the historicity of Gurbani and other Sikh Bani. Some portions contain atypical usage of modern-day Gurmukhi (e.g. tippi in place of bindi, unused yayya variations). In the past, ASCII fonts were used to render custom Gurmukhi (e.g. [Open Gurbani Akhar](https://github.com/GurbaniNow/gurmukhi-fonts)). As far as I knew, no such Unicode font existed to replace these ASCII fonts, so Sant Lipi was created.

Sant Lipi places the customized characters in [Private Use Areas](https://en.wikipedia.org/wiki/Private_Use_Areas). These characters or combos are unlikely to be accepted by the [Unicode Consortium](https://en.wikipedia.org/wiki/Unicode_Consortium), as they go against modern-day usage. Plenty examples exist of proposals asking for these characters to be added (e.g. [L2/20-076](https://www.unicode.org/L2/L2020/20076-gurmukhi-sum.pdf), [L2/20-183](https://www.unicode.org/L2/L2020/20183-gurmukhi-chg.pdf), etc.). So allocating these characters to Private Use Areas, to preserve Gurbani through Unicode, is the best option for now.

It should be noted, that Sant Lipi is a modification of [Mukta Mahee](https://github.com/EkType/Mukta) by [Ek Type](https://ektype.in/). As of writing, Mukta Mahee was the default Unicode font for Gurmukhi on Apple programs (i.e. iOS, iPad OS, macOS, Safari, etc.). Adding custom characters and ligatures is enough to faithfully represent all of the Gurmukhi in the Shabad OS Database.

The reason Shabad OS is committing to switch from ASCII to Unicode is simple. Over 99% of Shabad OS Database lines are faithfully represented using current Unicode standards. Percentage of all word instances increases very close to 100%. With Unicode, we will be able to better proofread the data directly. With Sant Lipi as our standard we also create stronger cohesion with our [Gurmukhi Utils](https://github.com/shabados/gurmukhi-utils) projects.

Sant Lipi is created using [Glyphs 3](https://glyphsapp.com/).

<!-- UFOs are generated with [glyphsLib](https://github.com/googlefonts/glyphsLib) for tracking changes. If contributing, please modify the glyphs file, and avoid changing the UFO files by hand.

## Todo

1. Set up exports / interpolations
2. Custom exports for VS Code
3. Potentially custom export for romanization (latin transliteration)
4. Set up GitHub Actions to automatically create releases based on glyphs file version
5. Create tests with html files
6. Create new PUA characters
7. Test on mobile repo
8. Convert from quadratic to beziers
9. Convert to variable font
10. Minimize nodes for maintenance (use overlapping shapes)
11. Modify characters to "open" their forms for legibility
12. Get to parity with Noto Sans Gurmukhi (e.g. nukta options)
13. ???
14. Profit

## Custom Characters

Work in progress. Currently in progress of converting the original FontLab files to Glyphs format.

## Installation

You can download the latest version of Sant Lipi from the [releases page](https://github.com/shabados/SantLipi/releases).

Sant Lipi can render Gurmukhi in [VS Code](https://code.visualstudio.com/) without affecting the source code. -->

## Community

The easiest way to communicate is via [GitHub issues](https://github.com/shabados/SantLipi/issues). Please search for similar issues regarding your concerns before opening a new issue.

Get organization updates for Shabad OS by following us on [Instagram](https://www.instagram.com/shabad_os/) and [Twitter](https://twitter.com/shabad_os/). We also invite you to join us on our public chat server hosted on [Slack](https://chat.shabados.com/).

Our intention is to signal a safe open-source community. Please help us foster an atmosphere of kindness, cooperation, and understanding. By participating, you agree to abide by the [Contributor Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).

If you have a concern that doesn't warrant opening a GitHub issue, please reach out to Bhajneet S.K. ([@bhajneet](https://github.com/bhajneet/)). Bhajneet is the author and lead maintainer of Sant Lipi.

_Special thanks_ to:

- [Ek Type](https://ektype.in/) for creating the original Mukta Mahee font (see [GitHub](https://github.com/EkType/Mukta)).
