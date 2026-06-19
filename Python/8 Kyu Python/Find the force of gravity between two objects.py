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
    
