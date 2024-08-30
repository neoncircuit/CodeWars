def get_number_from_string(st):
    numbers = ""
    for i in st:
        if i.isdigit():
            numbers += i          
    return int(numbers)
