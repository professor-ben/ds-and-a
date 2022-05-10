#!/usr/bin/env python3

'''
An insertion sort loops through each element in a list, and starting with the
first element, compares it to the second element. If the second element is
smaller, the current element is moved into its position. This continues
through the third, fourth, etc. elements of the list until all are sorted.
'''
def InsertionSort(list):
    # First pass once for each element in list
    for i in range(1, len(list)):
        # j at index below i
        j = i - 1
        # i is element following list at index j
        element_next = list[i]

        # Continue until element at j is less than next element
        while (list[j] > element_next) and (j >= 0):
            # Insert element at j into next position
            list[j + 1] = list[j]
            # Decrease j
            j -= 1
        
        # Insert saved element at i at index above j
        list[j + 1] = element_next
    
    # Return sorted list
    return list
