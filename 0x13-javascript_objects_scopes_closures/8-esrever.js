#!/usr/bin/node
exports.esrever = function (list) {
  const size = list.length;
  const reversed = [];
  for (let i = size - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
