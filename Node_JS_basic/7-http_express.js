const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  const header = 'This is the list of our students\n';
  countStudents(process.argv[2])
    .then((text) => {
      res.send(`${header}${text}`);
    })
    .catch((error) => {
      res.send(`${header}${error.message}`);
    });
});

app.listen(1245);

module.exports = app;
