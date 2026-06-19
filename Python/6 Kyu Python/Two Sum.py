def two_sum(numbers, target):
    for i in range(len(numbers)):
            for j in range(i+1, len(numbers)): # j is always ahead of i
                if numbers[i] + numbers[j] == target:
                    return [i, j]