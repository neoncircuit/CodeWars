export function parseF(s: string): number | null {
  const parsedValue = parseFloat(s);
  return Number.isNaN(parsedValue) ? null : parsedValue;
}