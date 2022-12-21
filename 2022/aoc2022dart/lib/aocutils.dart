import 'dart:io';

Iterable<String> readLines(String filename) {
  return File("../inputs/$filename")
      .readAsStringSync()
      .split("\n")
      .where((e) => e.isNotEmpty);
}
