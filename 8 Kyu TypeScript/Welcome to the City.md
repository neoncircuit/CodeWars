# Welcome to the City

## Instructions

Create a method that takes as input a name, city, and state to welcome a person. Note that `name` will be an array consisting of one or more values that should be joined together with one space between each, and the length of the `name` array in test cases will vary.

Example:
```
['John', 'Smith'], 'Phoenix', 'Arizona'
```

This example will return the string 
```
Hello, John Smith! Welcome to Phoenix, Arizona!
```

## Given Code
```
export const sayHello = (name: string[], city: string, state: string):string => {
  return '';
}
```

## My Solution
```
export const sayHello = (name: string[], city: string, state: string):string => {
  let full_name = name.join(" ");
  let message = `Hello, ${full_name}! Welcome to ${city}, ${state}!`;
  return message;
}
```