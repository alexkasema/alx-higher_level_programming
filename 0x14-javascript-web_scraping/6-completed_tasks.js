#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

const my_obj = {};
let obj;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    obj = JSON.parse(body);
    obj.forEach(result => {
      if (result.completed) {
        userid = result.userId;
        if (!(userid in my_obj)) {
          my_obj[userid] = 0;
        }
        my_obj[userid] += 1;
      }
    });
    console.log(my_obj);
  }
});
