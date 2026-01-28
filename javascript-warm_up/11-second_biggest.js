#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  let max = args[0];
  let second = -Infinity;

  for (const n of args) {
    if (n > max) {
      second = max;
      max = n;
    } else if (n < max && n > second) {
      second = n;
    }
  }

  console.log(second);
}
