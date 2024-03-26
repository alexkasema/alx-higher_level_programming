#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

let obj;
let movies = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    obj = JSON.parse(body);
    obj.results.forEach(result => {
      result.characters.forEach(c => {
        const split = c.split('/people/');
        if (split[1] === '18/') {
          movies++;
        }
      });
    });
    console.log(movies);
  }
});
