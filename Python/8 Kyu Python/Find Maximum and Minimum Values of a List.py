def minimum(arr: list[int]) -> int:
    #your code here...
    arr.sort()
    return arr[0]

def maximum(arr: list[int]) -> int:
    #...and here
    arr.sort()
    return arr[-1]