#!/usr/bin/node
let i = 0;
const count = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
	console.log('Missing number of occurences');
} else {
while (i < count) {
	console.log('test');
	i++;
}
}
