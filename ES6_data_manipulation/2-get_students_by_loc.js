export default function getStudentsByLocation(listOfStudents, city) {
  const newList = listOfStudents.filter((student) => student.location === city);
  return newList;
}
