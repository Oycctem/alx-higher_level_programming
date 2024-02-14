#!/usr/bin/node
let i = 0;
const count = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  while (i < count) {
    console.log('X'.repeat(count));
    i++;
  }
}
