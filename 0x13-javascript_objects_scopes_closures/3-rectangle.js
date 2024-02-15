#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let s = '';
    let a = 0;
    while (a < this.height) {
      const b = 0;
      while (b < this.width) {
        s += 'X';
        a++;
      }
      s += '\n';
      a++;
    }
    console.log(s);
  }
}
module.exports = Rectangle;
