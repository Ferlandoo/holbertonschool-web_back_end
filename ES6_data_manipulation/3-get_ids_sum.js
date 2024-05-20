export default function getStudentIdsSum(students) {
  const initialValue = 0;
  const sumOfId = students.reduce((accumulator, student) => accumulator + student.id, initialValue);
  return sumOfId;
}
