# Title of Problem

Your job is to find the gravitational force between two spherical objects (obj1 , obj2).

## input
Two arrays are given :
- arr_val (value array), consists of 3 elements
1. 1st element : mass of obj 1
2. 2nd element : mass of obj 2
3. 3rd element : distance between their centers

- arr_unit (unit array), consists of 3 elements
1. 1st element : unit for mass of obj 1
2. 2nd element : unit for mass of obj 2
3. 3rd element : unit for distance between their centers

mass units are :
- kilogram (kg)
- gram (g)
- milligram (mg)
- microgram (μg)
- pound (lb)

distance units are :
- meter (m)
- centimeter (cm)
- millimeter (mm)
- micrometer (μm)
- feet (ft)

## Note
value of G = 6.67 × 10−11 N⋅kg−2⋅m2

1 ft = 0.3048 m

1 lb = 0.453592 kg

return value must be Newton for force (obviously)

μ copy this from here to use it in your solution

# Given Code

```{python}
def solution(arr_val, arr_unit) :
    pass
```

# My Solution

```{python}
def solution(arr_val, arr_unit) :
    G = 6.67 * pow(10, -11)
    
    mass = {
        "kg": pow(10, 3),
        "g": 1,
        "mg": pow(10, -3),
        "μg": pow(10, -6),
        "lb": 0.453592 * pow(10, 3)
    }
    
    distance = {
        "m": 1,
        "cm": pow(10, -2),
        "mm": pow(10, -3),
        "μm": pow(10, -6),
        "ft": 0.3048 
    }
    
    m1 = arr_val[0] * mass[arr_unit[0]] / 1000  # convert to kg
    m2 = arr_val[1] * mass[arr_unit[1]] / 1000  # convert to kg

    r = arr_val[2] * distance[arr_unit[2]]

    force = G * (m1 * m2) / pow(r, 2)

    return force
    
```
