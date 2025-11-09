#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
if (args.length < 2) {
  console.log(0);
} else {
  const max = Math.max(...args);
  let second = -Infinity;
  for (let i = 0; i < args.length; i++) {
    if (args[i] < max && args[i] > second) {
      second = args[i];
    }
  }
  console.log(second);
}
