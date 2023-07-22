// Create a function getStudentIdsSum that returns the sum of all the student ids.
// It should accept a list of students (from getListStudents) as a parameter.
// You must use the reduce function on the array.
function getStudentIdsSum(students) {
  const value = students.map((student) => student.id);
  return value.reduce((accumulator, idValue) => accumulator + idValue, 0);
}
export default getStudentIdsSum;
