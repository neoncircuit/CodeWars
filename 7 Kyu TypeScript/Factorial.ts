export function factorial(n: number) {
  // your code here
  if (n < 0) {
    throw new Error("Factorial is not defined for negative numbers.");
  }
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;       
}