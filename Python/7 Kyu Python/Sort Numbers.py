def solution(nums):
    if nums is None or len(nums) == 0:
        return []
    else:
        sortedNums = sorted(nums)
        return sortedNums
