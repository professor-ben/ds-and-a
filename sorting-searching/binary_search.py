#!/usr/bin/env python3

def BinarySearch(list, item):
    '''
    A binary search finds an item in a sorted list. It begins at the midpoint
    of the list and moves either forward or backward, depending on where the
    item should be located in a sorted list.
    '''
    first = 0
    last = len(list) - 1
    found = False

    # Continue until the first and last searched indices meet or item is found
    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        else:
            # Move earlier or later based on placement in sorted list
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    # Return found (True) or not found (False)
    return found