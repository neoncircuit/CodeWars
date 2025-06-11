export function countRedBeads(n: number): number {
  //your code here
  if (n < 2) {
    return 0;
  }
  let result = (n - 1) * 2;
  return result;
}