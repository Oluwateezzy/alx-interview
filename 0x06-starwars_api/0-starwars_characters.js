#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

const filmUrl = 'https://swapi-api.alx-tools.com/api/films' + '/' + argv[2];

request(filmUrl, async (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;

  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        if (err) {
          console.log(err);
        }
        const ch = JSON.parse(body).name;
        console.log(ch);
        resolve();
      });
    });
  }
});
