from typing import List

def name_value(my_list: List[str]) -> List[int]:
    res = []

    for position, name in enumerate(my_list, start=1):
        letter_sum = 0

        for char in name:
            if char == ' ':
                continue
            letter_sum += ord(char) - 96
        calculated_value = letter_sum * position
        res.append(calculated_value)

    return res