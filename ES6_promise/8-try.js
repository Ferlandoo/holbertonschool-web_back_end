export default function divideFunction (numerator, denominator) {
  return new Promise((resolve, reject) => {
    if (denominator === 0) {
      reject(new Error('ZeroDivisionError'));
    } else {
      resolve(numerator / denominator);
    }
  });
}
