import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:loginpage/firebase_options.dart';
import 'package:loginpage/login_pages/auth_service.dart';
import 'package:loginpage/login_pages/login_page.dart';

import 'login_pages/sign_up_page.dart';
import 'login_pages/starter_page.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: AuthService(),
      routes: {
        '/starterpage': (context) => StarterPage(),
        '/loginpage': (context) => LogInPage(),
        '/signuppage': (context) => SignUpPage(),
      },
    );
  }
}
