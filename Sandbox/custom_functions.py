"""
Replacement of common functions
"""

def len_replacement(chars):
    """
    replacement for len()
    """
    length = 0
    for _ in chars:
        length+=1
    return length

def sum_replacement(list_of_nums):
    """
    replacement for sum() for list
    """
    sum_value = 0
    for value in list_of_nums:
        sum_value+= value
    return sum_value

def min_replacement(list_of_nums):
    """
    replacement for min() for list
    """
    min_value = 0
    for value in list_of_nums:
        if value <= min_value:
            min_value = value
    return min_value

def max_replacement(list_of_nums):
    """
    replacement for max() for list
    """
    max_value = 0
    for value in list_of_nums:
        if value >= max_value:
            max_value = value
    return max_value

def sort_replacement(array):
    """
    replacement for sort() for list
    """
    quicksort(array, 0, len_replacement(array)-1)

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi-1)
        quicksort(array, pi+1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i+1
            (array[i], array[j]) = (array[j], array[i])
    (array[i+1], array[high]) = (array[high], array[i+1])

    return i+1

def reverse_replacement(list_of_nums):
    """
    replacement for reverse() for list
    """
    new_list = []
    for value in list_of_nums:
        new_list.insert(0, value)
    return new_list


array = [1, 5, 3, 4, 18, 3, -1, 41, 23, 5, 23, 52, 123, 23, 5, 7, 324 ,8, -56]

print(len_replacement('hello'))
print(len_replacement(array))
print(sum_replacement(array))
print(min_replacement(array))
print(max_replacement(array))
print(reverse_replacement(array))

sort_replacement(array)

print(f'The sorted array looks like this: {array}')
