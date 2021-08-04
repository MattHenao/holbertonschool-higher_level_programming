#!/usr/bin/node
const argument = process.argv;
const oneValue = argument[2];

if (!isNaN(oneValue)) {
  console.log('My number: ' + oneValue);
} else {
  console.log('Not a number');
}
