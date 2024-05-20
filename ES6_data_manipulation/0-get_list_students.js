export default function getListStudents() {
  const firstStudent = {
    id: 1,
    name: 'Guillaume',
    location: 'San Francisco',
  };

  const secondStudent = {
    id: 2,
    name: 'James',
    location: 'Columbia',
  };

  const thirdStudent = {
    id: 5,
    name: 'Serena',
    location: 'Francisco',
  };

  return typeof [firstStudent, secondStudent, thirdStudent];
}
