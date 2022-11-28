#!/usr/bin/node
const count = process.argv.lenth;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
