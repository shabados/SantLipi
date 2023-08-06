import 'dart:ui';

import 'package:flutter/material.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatefulWidget {
  const MainApp({super.key});

  @override
  State<StatefulWidget> createState() => AppState();
}

class AppState extends State<StatefulWidget> {
  var fontWeight = FontWeight.normal;
  var fontWeightVar = 400.0;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        sliderTheme: SliderThemeData(
          showValueIndicator: ShowValueIndicator.always,
        ),
      ),
      home: Scaffold(
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Divider(),
            Text(
              'ਸੰਤ ਲਿੱਪੀ',
              style: TextStyle(
                fontSize: 32,
                fontFamily: 'SantLipi',
                fontWeight: fontWeight,
              ),
            ),
            Slider(
              value: fontWeight.value.toDouble(),
              label: fontWeight.value.toString(),
              min: 100,
              max: 900,
              divisions: 8,
              onChanged: (value) {
                setState(() {
                  fontWeight = FontWeight.values[(value ~/ 100) - 1];
                });
              },
            ),
            const Divider(),
            Text(
              'ਸੰਤ ਲਿੱਪੀ',
              style: TextStyle(
                fontSize: 32,
                fontFamily: 'SantLipiVF',
                fontVariations: [
                  FontVariation('wght', fontWeightVar),
                ],
              ),
            ),
            Slider(
              value: fontWeightVar,
              label: fontWeightVar.toStringAsFixed(0),
              min: 100,
              max: 900,
              onChanged: (value) {
                setState(() {
                  fontWeightVar = value;
                });
              },
            ),
            const Divider(),
          ],
        ),
      ),
    );
  }
}
