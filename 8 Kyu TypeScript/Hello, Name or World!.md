# Hello, Name or World!

## Instructions

Define a method hello that `returns` "Hello, Name!" to a given `name`, or says Hello, World! if name is not given (or passed as an empty String).

Assuming that `name` is a `String` and it checks for user typos to return a name with a first capital letter (Xxxx).

## Examples:
```
* With `name` = "john"  => return "Hello, John!"
* With `name` = "aliCE" => return "Hello, Alice!"
* With `name` not given 
  or `name` = ""        => return "Hello, World!"
```

## Given Code
```
export function hello(name = ''): string {
  return '';
}
```

## My Solution
```
export function hello(name = ''): string {
  if (name === '') {
    return "Hello, World!";
  }
  const capitalizedName = name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
  return `Hello, ${capitalizedName}!`;
}
```