def is_valid_dni(s: str) -> bool:
    # write code here.
    if len(s) != 9 or s == '': 
        return False
    
    nums = s[:-1]
    letter = s[-1]
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"    
    
    if not nums.isdigit():
        return False
    
    if not letter.isalpha():
        return False
    
    num = int(nums)
    return letters[num%23] == letter