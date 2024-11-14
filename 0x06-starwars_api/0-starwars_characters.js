#!/usr/bin/node

const request = require('request');

const mainUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function getData (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function printData () {
  try {
    const response = await getData(mainUrl);
    function execPrint (response) {
      const characters = JSON.parse(response).characters;
      const promises = [];

      for (let i = 0; i < characters.length; i++) {
        promises.push(getData(characters[i]));
      }

      Promise.all(promises)
        .then((output) => {
          for (let j = 0; j < output.length; j++) {
            console.log(JSON.parse(output[j]).name);
          }
        });
    }
    execPrint(response);
  } catch (error) {
    console.log(error);
  }
}

printData();

/*
request.get(mainUrl, function (error, response, body) {
  if (error) console.error(error);
  const data = JSON.parse(body);
  characters = data.characters;
  for (let i = 0; i < characters.length; i++) {
    request.get(characters[i], function (nerror, nresponse, nbody) {
      const charData = JSON.parse(nbody);
      console.log(charData.name);
    });
  }
});
*/
