#!/usr/bin/node
const request = require('request');
if (process.argv.length < 3) {
  console.log('Usage: node get_movie_characters.js <movie_id>');
  process.exit(1);
}
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(apiUrl, (_, response, body) => {
  const movie = JSON.parse(body);
  movie.characters.forEach(characterUrl => {
    request.get(characterUrl, (_, __, body) => {
      console.log(JSON.parse(body).name);
    });
  });
});
