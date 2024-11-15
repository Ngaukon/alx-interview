#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

// Check if a film ID is passed as a command line argument
if (process.argv.length > 2) {
  // Request the film data using the provided ID
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err); // Log any request error
    }
    // Extract the character URLs from the film data
    const charactersURL = JSON.parse(body).characters;
    
    // Map each character URL to a promise that fetches the character's name
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr); // Reject if there is an error fetching character
          }
          resolve(JSON.parse(charactersReqBody).name); // Resolve with character name
        });
      }));

    // Wait for all character names to be fetched and print them
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr)); // Log any error during the promise resolution
  });
}
