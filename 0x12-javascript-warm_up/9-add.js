#!/usr/bin/node
const { argv } = require('process');

if (isNaN(Number(argv[2])) || isNaN(Number(argv[3]))) {
  console.log('NaN');
} else {
  const a = Number(argv[2]);
  const b = Number(argv[3]);
  function add (a, b) {
    console.log(a + b);
  }
  add(a, b);
}
