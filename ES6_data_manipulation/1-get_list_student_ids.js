// Create a function getListStudentIds that returns an array of ids from a list of object.
// This function is taking one argument which is an array of objects
// - and this array is the same format as getListStudents from the previous task.
// If the argument is not an array, the function is returning an empty array.
// You must use the map function on the array.
function getListStudentIds(studentsArray) {
  if (!Array.isArray(studentsArray)) {
    return [];
  }

  return studentsArray.map((student) => student.id);
}

export default getListStudentIds;
