export default function hasValuesFromArray(argSet, argArray) {
  return argArray.every((value) => argSet.has(value));
}
