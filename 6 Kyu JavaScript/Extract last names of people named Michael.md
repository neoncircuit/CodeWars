# Extract last names of people named Michael

## Instructions

Given a text, for example:

`const inputText = "Michael, how are you? - Cool, how is John Williamns and Michael Jordan? I don't know but Michael Johnson is fine. Michael do you still score points with LeBron James, Michael Green AKA Star and Michael Wood?";`

get an array of last names of people named Michael. The result should be:
`["Jordan", "Johnson", "Green", "Wood"]`

## Notes:

- First name will always be Michael with upper case 'M'.

- There will always be a space character between 'Michael' and last name.

- Last name will always be one word, starting with an upper-case letter and continuing with lower-case letters.

- There will always be at least one 'Micheal' with a valid last name in the input text.


## Given Code
```javascript
function getMichaelLastName(inputText) {
  // your awesome code here
}
```

## My Solution
```javascript
function getMichaelLastName(inputText) {
  // your awesome code here
  
  // Use a regular expression to match "Michael <LastName>"
  const regex = /Michael ([A-Z][a-z]*)/g;
  
  // Extract matches using the regular expression
  const matches = [];
  let match;
  while ((match = regex.exec(inputText)) !== null) {
    matches.push(match[1]); // Push the last name (group 1) to the array
  }
  
  return matches;
}
```
