# Simple Fun #86: is Information Consistent?

## Instructions

## Task

Court is in session. We got a group of witnesses who have all taken an oath to tell the truth. The prosecutor is pointing at the defendants one by one and asking each witnesses a simple question - "guilty or not?". The witnesses are allowed to respond in one of the following three ways:

```
I am sure he/she is guilty.
I am sure he/she is innocent.
I have no idea.
```

The prosecutor has a hunch that one of the witnesses might not be telling the truth so she decides to cross-check all of their testimonies and see if the information gathered is consistent, i.e. there are no two witnesses A and B and a defendant C such that A says C is guilty while B says C is innocent.

## Example

For

```
evidences =  [[ 0, 1, 0, 1], 
               [-1, 1, 0, 0], 
               [-1, 0, 0, 1]]
```
               
the output should be `true`;

For

```
evidences =  [[ 1, 0], 
               [-1, 0], 
               [ 1, 1],
               [ 1, 1]]  
```

the output should be `false`.

## Input/Output

1. `[input]` 2D integer array `evidences`

2. 2-dimensional array of integers representing the set of testimonials. evidences[i][j] is the testimonial of the ith witness on the jth defendant. -1 means `"innocent"`, 0 means `"no idea"`, and 1 means `"guilty"`.

3. Constraints:

- `2 ≤ evidences.length ≤ 5,`

- `2 ≤ evidences[0].length ≤ 10.`

- `[output]` a boolean value

- `true` if the evidence is consistent, `false` otherwise.

## Given Code
```python
def is_information_consistent(evidences):
    pass
```

## My Solution
```python
def is_information_consistent(evidences) -> bool:
    # Transpose the matrix to check testimonies defendant-wise
    for j in range(len(evidences[0])):  # Iterate over defendants (columns)
        testimonies = [evidences[i][j] for i in range(len(evidences))]
        if 1 in testimonies and -1 in testimonies:  # Check for conflict
            return False
    return True  
```
