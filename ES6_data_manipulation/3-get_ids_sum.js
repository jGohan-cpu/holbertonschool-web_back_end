/* enlist-disable */
export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  const reduce = students.reduce((accumulator, currentValue) => accumulator + currentValue.id, 0);
  return reduce;
}
