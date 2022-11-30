#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (const x in list) {
    reverse.unshift(list[x]);
  }
  return (reverse);
};
