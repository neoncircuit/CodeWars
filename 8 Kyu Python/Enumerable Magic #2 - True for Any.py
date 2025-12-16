from typing import Callable, List, TypeVar, Any

def any_(lst: List[Any], func: Callable[[Any], bool]) -> bool: 
    """
    Check if func returns True for any item in the array
    
    Args:
        lst: typing.List[Any]
        func: typing.Callable[[Any], bool]
    
    Returns: 
        True if the callback returns True for ANY item.
        False if the list is empty or no items match.
    """
    for item in lst:
        if func(item):
            return True
            
    return False