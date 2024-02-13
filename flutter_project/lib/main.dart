import 'package:flutter/material.dart';
import 'package:loginpage/login_pages/login_page.dart';

import 'login_pages/sign_up_page.dart';
import 'login_pages/starter_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: SignUpPage(),
      routes: {
        '/starterpage': (context) => StarterPage(),
        '/loginpage': (context) => LogInPage(),
        '/signuppage': (context) => SignUpPage(),
      },
    );
  }
}
