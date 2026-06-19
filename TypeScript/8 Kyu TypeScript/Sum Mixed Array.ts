export function sumMix(x: any[]): number {
  let sum: number = 0;
  for (let i=0; i<x.length; i++) {
    sum += Number(x[i]);
  }
  return sum;
}