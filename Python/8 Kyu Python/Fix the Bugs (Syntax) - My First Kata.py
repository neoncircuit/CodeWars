def my_first_kata(a,b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a != 0 and b != 0:
            return (a % b) + (b % a)
    else:
        return False
