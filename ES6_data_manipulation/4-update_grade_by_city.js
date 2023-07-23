// Create a function updateStudentGradeByCity that returns
// an array of students for a specific city with their new grade
// it should accept a list of students (from getListStudents),
// a city (String), and newGrades (Array of “grade” objects)
// as parameters.
// newGrades is an array of objects with this format:
//  {
//    studentId: 31,
//    grade: 78,
//  }
// If a student doesn’t have grade in newGrades, the final grade should be N/A.
// You must use filter and map combined.
function updateStudentGradeByCity(students, city, newGrades) {
  const studentsInCity = students.filter((student) => student.location === city);
  const updatedStudents = studentsInCity.map((student) => {
    const gradeObj = newGrades.find((grade) => grade.studentId === student.id);

    if (gradeObj) {
      return { ...student, grade: gradeObj.grade };
    }
    return { ...student, grade: 'N/A' };
  });
  return updatedStudents;
}
export default updateStudentGradeByCity;
