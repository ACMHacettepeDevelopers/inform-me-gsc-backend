import 'package:flutter/material.dart';

class Tabbar extends StatefulWidget {
  const Tabbar({Key? key}) : super(key: key);

  @override
  State<Tabbar> createState() => _TabbarState();
}

class _TabbarState extends State<Tabbar> {
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 4,
      child: Scaffold(
        appBar: AppBar(
          title: const Text("tabbar"),
          backgroundColor: Color.fromRGBO(237, 230, 230, 1),
          bottom: const TabBar(
            tabs: [
              Tab(
                text: "Tech",
              ),
              Tab(
                text: "Politics",
              ),
              Tab(
                text: "Economy",
              ),
              Tab(
                text: "Sports",
              )
            ],
          ),
        ),
        body: const TabBarView(
          children: [
            Center(
              child: Text("Tech"),
            ),
            Center(
              child: Text("Politics"),
            ),
            Center(
              child: Text("Economy"),
            ),
            Center(
              child: Text("Sports"),
            ),
          ],
        ),
      ),
    );
  }
}
