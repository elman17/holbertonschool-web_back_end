export default function updateStudentGradeByCity(list, city, newGrades) {
  return list
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeInfo = newGrades.find(
        (grade) => grade.studentId === student.id,
      );

      return {
        ...student,
        grade: gradeInfo ? gradeInfo.grade : "N/A",
      };
    });
}
