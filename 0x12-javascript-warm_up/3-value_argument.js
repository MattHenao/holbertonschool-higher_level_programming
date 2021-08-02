#!/usr/bin/node
const arguments = process.argv;

if (arguments.length <= 2){
  console.log('No arguments');
} else{
  console.log(arguments[2])
}
