#!/usr/bin/node
let i = 0;
const count = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  while (i < count) {
    console.log('C is fun');
    i++;
  }
}
