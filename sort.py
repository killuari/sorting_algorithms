def bubbleSort(lst_int: list[int], lst: list) -> list:
    """
    Sorts a list of elements using the Bubble Sort algorithm.

    Parameters:
        l (list): The list of elements to be sorted.

    Returns:
        list: The sorted list of elements.
    """
    for i in range(len(lst_int)):
        for j in range(len(lst_int) - i - 1):
            if lst_int[j] > lst_int[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def doubleSelectionSort(lst_int: list[int], lst: list) -> list:
    """
    Sorts a given list using the double selection sort algorithm.

    Parameters:
        l (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(len(lst_int) // 2):
        min_val = float('inf')
        max_val = float('-inf')
        min_index = i
        max_index = -1 - i
        for j in range(i, len(lst_int) - i):
            if lst_int[j] < min_val:
                min_val = lst_int[j]
                min_index = j
            if lst_int[j] > max_val:
                max_val = lst_int[j]
                max_index = j
        lst[min_index], lst[i] = lst[i], min_val
        lst[max_index], lst[-1 - i] = lst[-1 - i], max_val

