export function hello(name = ''): string {
  if (name === '') {
    return "Hello, World!";
  }
  const capitalizedName = name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
  return `Hello, ${capitalizedName}!`;
}