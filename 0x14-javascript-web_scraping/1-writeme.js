#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const fileInput = process.argv[3];

fs.writeFile(file, fileInput, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
