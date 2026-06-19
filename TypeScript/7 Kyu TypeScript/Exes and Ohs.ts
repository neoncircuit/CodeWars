export function xo(str: string) : boolean {
  // your code here
  let countExes = 0;
  let countOhhs = 0;
  const lowercasedStr = str.toLowerCase();

  for (const char of lowercasedStr) {
    if (char === 'x') {
      countExes++;
    }
    if (char === 'o') {
      countOhhs++;
    }
  }
  return countExes === countOhhs;
}