export const sayHello = (name: string[], city: string, state: string):string => {
  let full_name = name.join(" ");
  let message = `Hello, ${full_name}! Welcome to ${city}, ${state}!`;
  return message;
}