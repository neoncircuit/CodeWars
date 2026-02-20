def status(nums: list[int]) -> list[int]:
    #let's crank some code!
    # Step 1. Sort the list of integers
    nums_sorted = sorted(nums)
    
    # Step 2. Map the value, how many numbers are smaller than the target number
    value_to_count_less = {}
    for idx, v in enumerate(nums_sorted):
        if v not in value_to_count_less:
            value_to_count_less[v] = idx
            
    # Step 3. Iterate original array and compute status for each element
    triples = []  # (status, original_index, value)
    for i, v in enumerate(nums):
        count_less = value_to_count_less[v]
        status = i + count_less
        triples.append((status, i, v))
        print(f"index={i}, value={v}, count_less={count_less}, status={status}")

    # Step 4. Sort by status then original index (tuples sort that way by default)
    triples.sort()

    # Step 5. Extract values in the new order
    return [v for _, _, v in triples]