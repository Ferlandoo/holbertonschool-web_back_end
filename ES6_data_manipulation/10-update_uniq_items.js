export default function updateUniqueItems(argMap) {
  if (!(argMap instanceof Map)) {
    throw Error('Cannot process');
  }
  argMap.forEach((value, key) => {
    if (value === 1) {
      argMap.set(key, 100);
    }
    return argMap;
  });
}
