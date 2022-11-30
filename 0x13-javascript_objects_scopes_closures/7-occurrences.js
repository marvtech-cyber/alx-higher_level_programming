#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0; let count = 0;
  while (list[i]) {
    if (searchElement === list[i]) {
      count += 1;
    }
    i++;
  }
  return (count);
};
