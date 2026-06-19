def pipe_fix(nums):
    fix = []
    minVal = min(nums)
    maxVal = max(nums)
    
    for i in range(minVal, maxVal+1):
        fix.append(i)
        
    return fix
