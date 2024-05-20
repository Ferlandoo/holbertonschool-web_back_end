export default function getListStudentIds(param) {
  if (!Array.isArray(param)) {
    return [];
  }
  const ids = param.map((item) => item.id);
  return ids;
}
