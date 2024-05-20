export default function cleanSet(argSet, startString) {
  if (startString.length === 0) {
    return '';
  }
  const cleanPart = new Set([...argSet].filter((text) => text.startsWith(startString)));
  const newStr = Array.from(cleanPart).join('-');
  return newStr.replace(new RegExp(startString, 'g'), '');
}
