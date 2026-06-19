export function correct(s: string): string{
  // your code here
  return s.replaceAll("5", "S")
          .replaceAll("0", "O")
          .replaceAll("1", "I");
}