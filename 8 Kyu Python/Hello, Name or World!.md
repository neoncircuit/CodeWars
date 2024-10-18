# Hello, Name or World!

## Instructions

Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

## Examples:
```
* With `name` = "john"  => return "Hello, John!"
* With `name` = "aliCE" => return "Hello, Alice!"
* With `name` not given 
  or `name` = ""        => return "Hello, World!"
```

## Given Code
```python
def hello(name):
    pass
```

## My Solution
```python
def hello(name=""):
    match name:
        case "" | None:
            return "Hello, World!"
        case _:
            capitalized_name = name.capitalize()
            return f"Hello, {capitalized_name}!"
```
