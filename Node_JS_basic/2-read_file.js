const fs = require("fs");

function countStudents(path) {
  let data;

  try {
    data = fs.readFileSync(path, "utf8");
  } catch (error) {
    throw new Error("Cannot load the database");
  }

  const students = data
    .split("\n")
    .slice(1)
    .filter((line) => line.trim() !== "");

  console.log(`Number of students: ${students.length}`);

  const studentsByField = {};

  students.forEach((student) => {
    const fields = student.split(",");
    const firstname = fields[0];
    const field = fields[3];

    if (!studentsByField[field]) {
      studentsByField[field] = [];
    }

    studentsByField[field].push(firstname);
  });

  Object.entries(studentsByField).forEach(([field, names]) => {
    console.log(
      `Number of students in ${field}: ${names.length}. List: ${names.join(", ")}`,
    );
  });
}

module.exports = countStudents;
