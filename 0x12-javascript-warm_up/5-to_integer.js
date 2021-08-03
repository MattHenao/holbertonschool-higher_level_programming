#!/usr/bin/node
const arguments = process.argv;
const oneValue = arguments[2];

if (!isNaN(oneValue)){
	console.log('My number: ' + oneValue);
} else{
	console.log('Not a number');
}
