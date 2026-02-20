class List:
    def remove_(self, integer_list: list[int], values_list: list[int]) -> list[int]:
        remove_ints = set(values_list)
        found = any(num in remove_ints for num in integer_list)
        integer_list[:] = [num for num in integer_list if num not in remove_ints]
        return integer_list