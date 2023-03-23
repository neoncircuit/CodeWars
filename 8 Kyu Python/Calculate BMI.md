Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

# Given Code
```{r test-python, engine='python'}
def bmi(weight, height):
    #your code here
```
# My Solution
```{r test-python, engine='python'}
def bmi(weight, height):
    #your code here 
    BMI = weight/height**2    
    #health = ""    
    if BMI <= 18.5:    
        health = "Underweight"        
    elif BMI <= 25.0:    
        health = "Normal"        
    elif BMI <= 30.0:    
        health = "Overweight"        
    elif BMI > 30.0:    
        health = "Obese"        
    return health
```
