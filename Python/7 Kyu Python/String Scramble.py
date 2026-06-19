def scramble(strng: str, array: list[int]) -> str:
    result_list = [''] * len(strng)
    
    for char, index in zip(strng, array):
        result_list[index] = char
        
    return "".join(result_list)