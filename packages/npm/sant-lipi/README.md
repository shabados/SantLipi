# Sant Lipi

A [unicode](<https://en.wikipedia.org/wiki/Gurmukhi_(Unicode_block)>) font for extraordinary [Gurmukhi](https://en.wikipedia.org/wiki/Gurmukhi).

Sant Lipi is a [variable font](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_Fonts_Guide) with the purpose of fully expressing the unique characters and combos found in the [database](https://github.com/shabados/database) at [Shabad OS](https://shabados.com/).

Please see Sant Lipi's [GitHub](https://github.com/shabados/SantLipi) repo to learn more.

## Installation

```shell
npm install sant-lipi
```

## Usage

Import it in your app entry file or component.

```js
import 'sant-lipi'
```

Reference the font name in a stylesheet, css-in-js, etc.

```css
font-family: 'Sant Lipi';
```

Note: Only use numerals to define the weight (avoid using 'lighter', 'normal', or 'bold'). The font weight varies from 100 to 900.

Note: All modern browsers support variable fonts. Instanced fonts are not bundled for fallback in this package. See ["Can I use variable fonts?"](https://caniuse.com/variable-fonts) for browser support.

Note: If you require legacy browser support, then please avoid using this package. See the [web.dev article on variable fonts](https://web.dev/variable-fonts/) for more help with legacy browsers. You can find the interpolated files in the [Sant Lipi repo](https://github.com/shabados/SantLipi).
