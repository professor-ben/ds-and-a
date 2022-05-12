#!/usr/bin/env python3


def BubbleSort(list):
    '''
    A bubble sort is the most rudimentary type of sorting algorithm. It loops
    through each index of the input list in descending order and swaps any
    items through that index that are out of order. On each iteration, the
    greatest number in the input list is moved all the way to the right. This
    continues until there is only the leftmost (smallest) element in the list.
    '''
    # The index of the last element is one less than the list's length
    lastElementIndex = len(list) - 1
    
    # In first pass, loop through each element of list in descending order
    for passNo in range(lastElementIndex, 0, -1):
        # In second pass, loop through each indexed element in list 
        for idx in range(passNo):
            # If indexed element is greater than next element, swap the two
            if list[idx] > list[idx + 1]:
                list[idx], list[idx + 1] = list[idx + 1], list[idx]
    
    # Return sorted list
    return list
