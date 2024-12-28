def enough(cap:int, on:int, wait:int) -> int:
    # Your code here
    return 0 if (on+wait) < cap else abs(cap-on-wait)