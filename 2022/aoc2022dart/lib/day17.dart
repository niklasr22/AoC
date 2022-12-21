import 'dart:collection';
import 'dart:math';

import 'aocutils.dart';
import 'package:tuple/tuple.dart';

Set<Tuple2<int, int>> moveRock(
    Set<Tuple2<int, int>> rock, Set<Tuple2<int, int>> cave,
    {int x = 0, int y = 0}) {
  Set<Tuple2<int, int>> newRock = {};
  for (var pos in rock) {
    var newRockPartPos = Tuple2(pos.item1 + x, pos.item2 + y);
    if (newRockPartPos.item1 < 0 ||
        newRockPartPos.item1 > 6 ||
        cave.contains(newRockPartPos)) return rock;
    newRock.add(newRockPartPos);
  }
  return newRock;
}

int run(int totalRocks) {
  String jet = readLines("day17.txt").first;
  List<Set<Tuple2<int, int>>> rockShapes = [
    {Tuple2(2, 0), Tuple2(3, 0), Tuple2(4, 0), Tuple2(5, 0)}, // horizontal line
    {
      Tuple2(3, 2),
      Tuple2(2, 1),
      Tuple2(3, 1),
      Tuple2(4, 1),
      Tuple2(3, 0)
    }, // cross
    {
      Tuple2(4, 2),
      Tuple2(4, 1),
      Tuple2(2, 0),
      Tuple2(3, 0),
      Tuple2(4, 0)
    }, // mirrored L
    {Tuple2(2, 3), Tuple2(2, 2), Tuple2(2, 1), Tuple2(2, 0)}, // vertical line
    {Tuple2(2, 1), Tuple2(3, 1), Tuple2(2, 0), Tuple2(3, 0)} // 2x2 block
  ];

  Set<Tuple2<int, int>> cave = {};
  cave.addAll([
    Tuple2(0, 0),
    Tuple2(1, 0),
    Tuple2(2, 0),
    Tuple2(3, 0),
    Tuple2(4, 0),
    Tuple2(5, 0),
    Tuple2(6, 0)
  ]);
  var jetIndex = 0;
  var cache = HashMap<Tuple2<int, int>, Tuple2<int, int>>();
  int height = 0;
  for (var rockCounter = 0; rockCounter < totalRocks; rockCounter++) {
    var rockIndex = rockCounter % rockShapes.length;
    var rock = moveRock(rockShapes[rockIndex], cave, y: height + 4);
    var firstMove = true;
    while (true) {
      var move = jet[jetIndex];

      if (rockCounter > 1000 && firstMove) {
        firstMove = false;
        var cacheKey = Tuple2(rockIndex, jetIndex);
        if (cache.containsKey(cacheKey)) {
          var cachedRock = cache[cacheKey]!;
          var period = rockCounter - cachedRock.item2;
          var heightPerPeriod = height - cachedRock.item1;
          if (totalRocks % period == rockCounter % period) {
            height = cachedRock.item1 +
                (((totalRocks - rockCounter) / period).floor() + 1) *
                    heightPerPeriod;
            return height;
          }
        } else {
          cache[cacheKey] = Tuple2(height, rockCounter);
        }
      }

      jetIndex = (jetIndex + 1) % jet.length;

      var newRock = move == ">"
          ? moveRock(rock, cave, x: 1)
          : moveRock(rock, cave, x: -1);
      var newestRock = moveRock(newRock, cave, y: -1);

      if (newRock == newestRock) {
        cave.addAll(newestRock);
        for (var x in cave) {
          height = max(height, x.item2);
        }
        break;
      }
      rock = newestRock;
    }
  }
  return height;
}
