#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching film data:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error fetching film data. Status code:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  characterUrls.forEach((characterUrl) => {
    request.get(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character data:', charError);
        return;
      }

      if (charResponse.statusCode === 200) {
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      } else {
        console.error('Error fetching character data. Status code:', charResponse.statusCode);
      }
    });
  });
});
