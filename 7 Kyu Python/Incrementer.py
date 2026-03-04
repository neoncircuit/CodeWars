def incrementer(nums: list[int]) -> list[int]:
    # your code here
    res = []
    for index, num in enumerate(nums, start=1):
        res.append((num+index)%10)
    return res