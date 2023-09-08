#!/usr/bin/node

/**
 * print all start wars movive character
 */

const request = require('request');
const { argv } = require('process');

const filmUrl = 'https://swapi-api.alx-tools.com/api/films' + '/' + argv[2];
// make api request
request(filmUrl, async (err, res, body) => {
  if (err) {
    console.error(err);
  }
  const characters = JSON.parse(body).characters;

  for (const character of characters) {
    // wait for each request
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        if (err) {
          console.error(err);
        }
        const ch = JSON.parse(body).name;
        console.log(ch);
        resolve();
      });
    });
  }
});
