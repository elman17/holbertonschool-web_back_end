export default function getStudentIdSum(list) {
  return list.reduce((sum, student) => sum + student.id, 0);
}
