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