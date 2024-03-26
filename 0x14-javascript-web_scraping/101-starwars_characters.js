#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(filmUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmObj = JSON.parse(body);
    try {
      await Promise.all(filmObj.characters.map(async (c) => {
        const character = await getRequestData(c);
        console.log(character.name);
      }));
    } catch (err) {
      console.error(err);
    }
  }
});

function getRequestData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const data = JSON.parse(body);
        resolve(data);
      }
    });
  });
}
