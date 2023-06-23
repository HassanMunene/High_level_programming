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
        process.stdout.write('X');
      }
      console.log();
    }
  }
    double () {
        let h = this.height * 2;
        let w = this.width * 2;
        for (let i = 1; i <= h; i++) {
            for (let j = 1; j <= w; j++) {
                process.stdout.write('X');
            }
            console.log();
        }
    }
}
module.exports = Rectangle;
