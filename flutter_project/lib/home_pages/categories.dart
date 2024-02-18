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
        appBar: PreferredSize(
          preferredSize: Size.fromHeight(kToolbarHeight + 56),
          child: SafeArea(
            child: Column(
              children: [
                TabBar(
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
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: TextField(
                    decoration: InputDecoration(
                      hintText: 'Search',
                      prefixIcon: Icon(Icons.search),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
        body: TabBarView(
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
