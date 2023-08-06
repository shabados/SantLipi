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
  var fontWeight = 400.0;

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
            Text(
              'ਸੰਤ ਲਿੱਪੀ',
              style: TextStyle(
                fontSize: 32,
                fontFamily: 'SantLipi',
                fontVariations: [
                  FontVariation('wght', fontWeight),
                ],
              ),
            ),
            Slider(
              value: fontWeight,
              label: fontWeight.toStringAsFixed(0),
              min: 100,
              max: 900,
              onChanged: (value) {
                setState(() {
                  fontWeight = value;
                });
              },
            ),
          ],
        ),
      ),
    );
  }
}
