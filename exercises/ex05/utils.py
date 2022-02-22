"""Utils."""

___author___ = "730474696"


def only_evens(evens: list[int]) -> list[int]:
    """Returns only the even numbers in a list of ints."""
    i: int = 0
    evens_list: list[int] = []
    while i < len(evens):
        if (evens[i] % 2) == 0:
            evens_list.append(evens[i])
        i += 1
    return evens_list


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a list with only the values found between start_index and end_index."""
    i: int = start_index 
    a: int = end_index
    b_list: list[int] = []
    if start_index < 0:
        i = 0
    if end_index > len(a_list):
        a = (len(a_list))
    while i < a:
        b_list.append(a_list[i])
        i += 1
    return b_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Returns one list with all of first_list followed by all of second_list."""
    i: int = 0
    a: int = 0
    new_list: list[int] = []
    while i < len(first_list):
        new_list.append(first_list[i])
        i += 1
    while a < len(second_list):
        new_list.append(second_list[a])
        a += 1
    return new_list


list_one: list[int] = [1, 3, 5, 8]
list_two: list[int] = [9, 5, 7, 10]
print(only_evens(list_one))
print(sub(list_one, 0, 4))
print(concat(list_one, list_two))