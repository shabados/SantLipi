# Sant Lipi

A [unicode](<https://en.wikipedia.org/wiki/Gurmukhi_(Unicode_block)>) font for extraordinary [Gurmukhi](https://en.wikipedia.org/wiki/Gurmukhi).

Sant Lipi is a [variable font](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_Fonts_Guide) with the purpose of fully expressing the unique characters and combos found in the [database](https://github.com/shabados/database) at [Shabad OS](https://shabados.com/).

Please see Sant Lipi's [GitHub](https://github.com/shabados/SantLipi) repo to learn more.

## Installation

```shell
dart pub get sant_lipi
```

## Usage

Add the font in `pubspec.yaml` of your project.
```yaml
flutter:
  fonts:
    - family: SantLipi
      fonts:
        - asset: packages/sant_lipi/SantLipi-Black.ttf
        - asset: packages/sant_lipi/SantLipi-Bold.ttf
        - asset: packages/sant_lipi/SantLipi-ExtraBold.ttf
        - asset: packages/sant_lipi/SantLipi-ExtraLight.ttf
        - asset: packages/sant_lipi/SantLipi-Light.ttf
        - asset: packages/sant_lipi/SantLipi-Medium.ttf
        - asset: packages/sant_lipi/SantLipi-Regular.ttf
        - asset: packages/sant_lipi/SantLipi-SemiBold.ttf
        - asset: packages/sant_lipi/SantLipi-Thin.ttf
    - family: SantLipiVF # Variable Font
      fonts:
        - asset: packages/sant_lipi/SantLipi-VF.ttf
```

Use the static weight font:

```dart
TextStyle(
  fontFamily: 'SantLipi',
  fontWeight: FontWeight.w400,
)
```

Use the variable weight font:

```dart
TextStyle(
  fontFamily: 'SantLipiVF',
  fontVariations: [
    FontVariation('wght', 400),
  ],
)
```

See Flutter docs: [Use a custom font](https://docs.flutter.dev/cookbook/design/fonts).
