#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

const myObj = {};
let obj;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    obj = JSON.parse(body);
    obj.forEach(result => {
      if (result.completed) {
        const userid = result.userId;
        if (!(userid in myObj)) {
          myObj[userid] = 0;
        }
        myObj[userid] += 1;
      }
    });
    console.log(myObj);
  }
});
