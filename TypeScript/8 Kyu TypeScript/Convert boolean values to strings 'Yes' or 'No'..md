# Convert boolean values to strings 'Yes' or 'No'.

## Instructions

Complete the method that takes a boolean value and return a `"Yes"` string for `true`, or a `"No"` string for `false`.

## Given Code
```
export const boolToWord = (bool: boolean): string => {
  throw new Error("Not implemented!");
};
```

## My Solution
```
export const boolToWord = (bool: boolean): string => {
  let con = " ";
  if (bool) {
    con = "Yes";  
  } else {
    con = "No";
  }
  return con;
};
```