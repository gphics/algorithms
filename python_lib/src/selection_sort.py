from typing import List

def find_smallest(arr:List[int]) -> int:
    """
    This function finds the smallest number and return it's index

    Params:
        arr: a list of unsorted integers

    Returns:
        The index of the smallest integer in the arr
    """

    # getting the first element of the arr
    smallest = arr[0]
    # settin the default smallest index
    smallest_index = 0

    # looping ...
    for i in range(1, len(arr)):

        # checking if the current arr element is less than the previous smallest 
        if arr[i] < smallest:
            # if true
            smallest = arr[i]
            smallest_index = i
    return smallest_index



def selection_sort(arr:List[int]) -> List[int]:
    """
    This function takes an unsorted list

    Params:
        arr: a list of unsorted integers

    Returns:
        A sorted list
    """

    # performing type checks on the arr
    if not all( isinstance(elem , int) for elem in arr):
            raise TypeError("Only integer type is accepted as a valid arr element")
    
    copied_arr = list(arr)
    sorted_arr = []

    # looping ...
    for _ in range(len(copied_arr)):
        # getting the smallest index in the arr
        smallest_index = find_smallest(copied_arr)
        # updating the sorted arr
        sorted_arr.append(copied_arr.pop(smallest_index))

    return sorted_arr




