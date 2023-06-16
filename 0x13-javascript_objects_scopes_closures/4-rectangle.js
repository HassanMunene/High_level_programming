#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w === 0 || h === 0 || w < 1 || h < 1 || w === undefined || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print() {
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        process.stdout.write('x');
      }
      console.log();
    }
  }

  double() {
    for (let i = 1; i <= this.height * 2; i++) {
      for (let j = 1; j <= this.width * 2; j++) {
        process.stdout.write('x');
      }
      console.log();
    }
  }

  rotate() {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

module.exports = Rectangle;


