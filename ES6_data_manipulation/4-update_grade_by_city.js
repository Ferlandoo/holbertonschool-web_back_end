export default function updateStudentGradeByCity(listOfStudent, city, newGrade) {
  const filterStudent = listOfStudent.filter((student) => student.location === city);
  const addGrade = filterStudent.map((student) => {
    const grade = newGrade.find((grade) => grade.studentId === student.id);
    if (grade) {
      // eslint-disable-next-line no-param-reassign
      student.grade = grade.grade;
    } else {
      // eslint-disable-next-line no-param-reassign
      student.grade = 'N/A';
    }
    return student;
  });
  return addGrade;
}
