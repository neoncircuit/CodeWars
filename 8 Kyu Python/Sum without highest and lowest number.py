def sum_array(arr: list[int]) -> int:
    #your code here
    if not arr or len(arr) <= 2:
        return 0
    else: 
        arr.sort()
        return sum(arr[1:-1])