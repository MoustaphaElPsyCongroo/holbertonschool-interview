#!/usr/bin/node
const request = require('request');
const args = process.argv;

const getChar = () => {
  return new Promise((resolve, reject) => {
    request(`https://swapi-api.hbtn.io/api/films/${args[2]}`, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const data = JSON.parse(body);
        resolve(data.characters);
      }
    });
  });
};

const getName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const data = JSON.parse(body);
        console.log(data.name);
        resolve(data.name);
      }
    });
  });
};

const printNames = async () => {
  try {
    const arrName = await getChar();

    for (const element of arrName) {
      await getName(element);
    }
  } catch (error) {
    console.log(error);
  }
};

printNames();
