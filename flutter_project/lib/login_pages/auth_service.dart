import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:loginpage/home_pages/home_page_m.dart';
import 'package:loginpage/home_pages/home_page.dart';
import 'package:loginpage/login_pages/login_page.dart';

class AuthService extends StatelessWidget {
  const AuthService({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: StreamBuilder<User?>(
      stream: FirebaseAuth.instance.authStateChanges(),
      builder: ((context, snapshot) {
        if (snapshot.hasData) {
          return Home(); 
        } else {
          return LogInPage();
        }
      }),
    ));
  }
}
