export function isPalindrome(x: string): boolean {
  const lower = x.toLowerCase();
  const reversed = lower.split('').reverse().join('');
  return lower === reversed ? true : false;
}