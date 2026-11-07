const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const header = 'This is the list of our students\n';
    countStudents(process.argv[2])
      .then((text) => {
        res.end(`${header}${text}`);
      })
      .catch((error) => {
        res.end(`${header}${error.message}`);
      });
  } else {
    res.statusCode = 404;
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;
