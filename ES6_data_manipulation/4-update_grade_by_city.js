/* enlist-disable */
export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }

  const filter = students.filter((filteredObj) => filteredObj.location === city);
  const map = filter.map((mappedObj) => {
    const grade = newGrades.filter((newGradesObj) => newGradesObj.studentId === mappedObj.id);
    const newObj = { ...mappedObj };
    if (grade[0]) {
      newObj.grade = grade[0].grade;
    } else {
      newObj.grade = 'N/A';
    }
    return newObj;
  });
  return map;
}
