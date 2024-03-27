#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (_, response, body) => {
  const films = JSON.parse(body).results;
  const wedgeMovies = films.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
  console.log(wedgeMovies.length);
});
