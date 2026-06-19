def print_array(arr):
    if not arr:
        return ""
    # Convert each element to a string and then join them
    return ','.join(map(str, arr))
