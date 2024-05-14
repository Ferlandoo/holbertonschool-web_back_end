export default function uploadPhoto(filename) {
  return new Promise((resolve, reject) => {
    resolve(filename);
    reject(new Error(`${filename} cannot be processed`));
  });
}
