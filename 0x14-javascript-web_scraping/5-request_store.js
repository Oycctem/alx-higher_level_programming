#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request.get(process.argv[2], { encoding: 'utf-8' }, (_, response, body) => {
  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) console.error(err);
    else console.log(`Successfully stored the contents of ${process.argv[2]} in ${process.argv[3]}`);
  });
});
