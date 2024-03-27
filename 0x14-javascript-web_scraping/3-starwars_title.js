#!/usr/bin/node
const request = require('request');
request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (_, response, body) => {
  console.log(JSON.parse(body).title);
});
