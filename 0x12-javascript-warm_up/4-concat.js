#!/usr/bin/node
const arguments = process.argv;
oneValue = arguments[2];
twoValue = arguments[3];

if (arguments[2] <= 0){
	oneValue = 'undefined';
}
if (arguments[3] <= 0){
	twoValue = 'undefined';
}
console.log(oneValue + ' is ' +twoValue)
