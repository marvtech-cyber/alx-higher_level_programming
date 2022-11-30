#!/usr/bin/node
// Write a class Square that defines a square and inherits from Rectangle
const SquareR = require('./5-square');
module.exports = class Square extends SquareR {
  charPrint (c) {
    let i = 0;
    if (c === undefined) { c = 'X'; }
    while (i < this.width) {
      console.log(c.repeat(this.height));
      i++;
    }
  }
};
