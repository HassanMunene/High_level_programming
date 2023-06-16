#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === 0 || h === 0 || w < 1 || h < 1 || w === undefined || h === undefined) {
      return this;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        process.stdout.write('x');
      }
      console.log();
    }
  }
}
module.exports = Rectangle;
