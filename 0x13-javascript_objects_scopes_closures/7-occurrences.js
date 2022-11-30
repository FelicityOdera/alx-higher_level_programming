#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const x = searchElement;
  const n = list.length;
  let res = 0;
  for (let i = 0; i < n; i++) {
    if (x === list[i]) { res++; }
  }
  return res;
};
