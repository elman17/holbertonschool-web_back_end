const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    const onRead = (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1).map((line) => line.split(','));

      const output = [`Number of students: ${students.length}`];

      const fields = {};
      students.forEach((student) => {
        const firstname = student[0];
        const field = student[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      Object.keys(fields).forEach((field) => {
        const list = fields[field];
        output.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      });

      output.forEach((line) => console.log(line));
      resolve(output.join('\n'));
    };

    try {
      fs.readFile(path, 'utf8', onRead);
    } catch (err) {
      reject(new Error('Cannot load the database'));
    }
  });
}

module.exports = countStudents;