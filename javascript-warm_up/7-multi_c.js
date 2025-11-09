#!/usr/bin/node

const n = parseInt(process.argv[2]);
if (isNaN(n)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
