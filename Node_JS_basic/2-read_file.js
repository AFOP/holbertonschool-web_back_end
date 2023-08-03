// Using the database database.csv (provided in project description), create a function countStudents in the file 2-read_file.js
// Create a function named countStudents. It should accept a path in argument
// The script should attempt to read the database file synchronously
// If the database is not available, it should throw an error with the text Cannot load the database
// If the database is available, it should log the following message to the console Number of students: NUMBER_OF_STUDENTS
// It should log the number of students in each field, and the list with the following format: Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES
// CSV file can contain empty lines (at the end) - and they are not a valid student! 
const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    // read data
    const data = fs.readFileSync(path, { encoding: 'utf-8' });
    // split data and taking only list without header
    const lines = data.split('\n').slice(1, -1);
    // give the header of data
    const header = data.split('\n').slice(0, 1)[0].split(',');
    // find firstname and field index
    const idxFn = header.findIndex((ele) => ele === 'firstname');
    const idxFd = header.findIndex((ele) => ele === 'field');
    // declarate two dictionaries for count each fields and store list of students
    const fields = {};
    const students = {};

    lines.forEach((line) => {
      const list = line.split(',');
      if (!fields[list[idxFd]]) fields[list[idxFd]] = 0;
      fields[list[idxFd]] += 1;
      if (!students[list[idxFd]]) students[list[idxFd]] = '';
      students[list[idxFd]] += students[list[idxFd]] ? `, ${list[idxFn]}` : list[idxFn];
    });

    console.log(`Number of students: ${lines.length}`);
    for (const key in fields) {
      if (Object.hasOwnProperty.call(fields, key)) {
        const element = fields[key];
        console.log(`Number of students in ${key}: ${element}. List: ${students[key]}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};
