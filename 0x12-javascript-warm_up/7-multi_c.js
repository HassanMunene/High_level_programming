#!/usr/bin/node
const { argv } = require('process');

if (isNaN(Number(argv[2]))) {
  console.log('Missing number of occurrences');
} else 
{
	let i = 1;
	let x = Number(argv[2]);
	for (i; i <= x; i++)
	{
		console.log('C is fun');
	}
}
