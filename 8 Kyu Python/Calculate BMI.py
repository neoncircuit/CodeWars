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
