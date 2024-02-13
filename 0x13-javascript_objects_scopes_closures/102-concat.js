#!/usr/bin/node

const { readFile, writeFile } = require('fs');

const argv = process.argv;

const fileA = argv[2];
const fileB = argv[3];
const fileC = argv[4];

readFile(fileA, 'utf8', (err, result) => {
  if (err) {
    return;
  }
  const text1 = result;

  readFile(fileB, 'utf8', (err, result) => {
    if (err) {
      return;
    }
    const text2 = result;

    writeFile(fileC, text1 + text2, { flag: 'a' }, () => {});
  });
});
