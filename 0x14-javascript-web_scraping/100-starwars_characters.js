#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

let obj;
let name;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    obj = JSON.parse(body);
    obj.characters.forEach(c => {
      request(c, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          name = JSON.parse(body);
          console.log(name.name);
        }
      });
    });
  }
});
