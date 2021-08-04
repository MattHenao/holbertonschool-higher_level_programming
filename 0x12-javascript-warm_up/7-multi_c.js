#!/usr/bin/node
const prueba = process.argv.slice(2);

if (isNaN(parseInt(prueba[0]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < prueba; i++) {
    console.log('C is fun');
  }
}
