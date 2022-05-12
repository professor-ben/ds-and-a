#!/usr/bin/env python3

def SelectionSort(list):
    '''
    A selection sort looks at the length of a list and moves the largest
    element of the list to the top index on every pass through. After moving
    any element, the slot to be filled is moved one closer to the beginning.
    '''
    # In outer pass, move backward through indices of list
    for fill_slot in range(len(list) - 1, 0, -1):
        # Location of max value in list
        max_index = 0

        # In inner pass, move forward through indixes in list
        for location in range(1, fill_slot + 1):
            # Determine index of largest number in list
            if list[location] > list[max_index]:
                max_index = location

        # Swap value at fill_slot with max value in list
        list[fill_slot], list[max_index], = list[max_index], list[fill_slot]

    # Return sorted list
    return list
