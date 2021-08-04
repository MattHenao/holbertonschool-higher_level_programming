#!/usr/bin/node
function add (a, b) {
  return (a + b);
}

const argument = process.argv;

const numberOne = parseInt(argument[2]);
const numberTwo = parseInt(argument[3]);

console.log(add(numberOne, numberTwo));
