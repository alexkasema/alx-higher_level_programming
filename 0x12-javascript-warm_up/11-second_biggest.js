#!/usr/bin/node

const argv = process.argv;
const argc = process.argv.length;

if (argc < 4) {
  console.log(0);
} else {
  const myList = argv.slice(2).sort((a, b) => b - a);
  console.log(myList[1]);
}
