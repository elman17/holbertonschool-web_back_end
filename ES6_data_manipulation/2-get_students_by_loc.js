export default function getStudensByLocation(list, city) {
  return list.filter((student) => student.location === city);
}
