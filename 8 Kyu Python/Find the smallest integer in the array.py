def find_smallest_int(arr):
    # Code here
    small = arr[0];
    for i in range(0, len(arr)):
        if(arr[i] < small):    
            small = arr[i];
    return small
