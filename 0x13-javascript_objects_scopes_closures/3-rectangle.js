#!/usr/bin/node
// Write a class Rectangle that defines a rectangle
// If w or h is equal to 0 or not a positive integer, create an empty object
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && w !== undefined && h !== undefined) {
      this.width = w;
      this.height = h;
    }
  }

  // method print
  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }
};
