#!/usr/bin/env python3


def LinearSearch(list, item):
    '''
    A linear search is the simplest type of search. A loop checks every index,
    starting at 0, until the item is found or the end of the list is reached.
    '''
    index = 0
    found = False
    
    # Start at index 0 and loop through list until found
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index += 1

    # Return found (True) or not found (False)
    return found
