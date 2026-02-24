from collections.abc import Callable
from typing import Any, List

def processor_decorator(func:Callable[[List[int| float]], List[int| float]]) -> Callable[..., Any]:
    """
    This decorator checks if the received list only contain numbers and then sort it

    Params:
        func: The main function automatically passed by python under the hood

    Returs:
        It returns the wrapper function

    """
    def wrapper(*args):
        num_list = args[0]
        target = args[1]
        # checking the list content if it's int or float
        if not all(isinstance(current, (int, float)) for current in num_list):
            raise TypeError("The list can only contain numbers")
        
        # sorting the list
        sorted_arg = sorted(num_list)

        # calling and returning the result of the main function
        return func(sorted_arg, target)
    
    # returning the wrapper function
    return wrapper

@processor_decorator
def binary_search(arr:List[int | float], target:int | float) -> int | None:
    """
    This function use the binary search algorithm to search for a specific number in a list

    Params:
        arr: A list containing numbers. The list is expected to be sorted but if not sorted, the function sort it before use.
        target: An integer or float number that is been searched for in the arr

    Returns:
        The function return None if the target number is not in the arr but returns the index of the target if present.
    
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
        pass

    return None
    
