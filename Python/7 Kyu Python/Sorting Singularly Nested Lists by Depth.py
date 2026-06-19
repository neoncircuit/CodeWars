from typing import List, TypeAlias

# 1. Define the Recursive Type
# We define a type that is a list containing items of its own type.
# This represents: [], [[]], [[[]]], etc.
SingularNestedList: TypeAlias = list["SingularNestedList"]

def get_depth(nested_list: SingularNestedList) -> int:
    """
    Calculates the nesting depth of a singularly nested list.

    The depth is determined by peeling back layers until an empty list is found.
    - []       -> Depth 1
    - [[]]     -> Depth 2
    - [[[]]]   -> Depth 3

    Args:
        nested_list (SingularNestedList): The nested list to measure.

    Returns:
        int: The depth of the nesting (1-based).
    """
    depth: int = 1
    current: SingularNestedList = nested_list

    # Iterate while the current list is not empty
    while len(current) > 0:
        depth += 1
        # Move one layer deeper. We assume the list strictly contains
        # one item (the next list) based on problem constraints.
        current = current[0]
        
    return depth

def sort_by_depth(main_list: List[SingularNestedList]) -> List[SingularNestedList]:
    """
    Sorts a list of nested arrays in ascending order based on their depth.

    This function is stable and does not modify the original list in place
    if assigned to a new variable (though .sort() uses the reference).

    Args:
        main_list (List[SingularNestedList]): A list containing multiple nested lists.

    Returns:
        List[SingularNestedList]: The list sorted from shallowest to deepest.
    """
    # We use Python's built-in sort (Timsort) which is O(N log N).
    # We pass 'get_depth' as the key, so the sort is based on the integer returned by that function.
    main_list.sort(key=get_depth)
    
    return main_list