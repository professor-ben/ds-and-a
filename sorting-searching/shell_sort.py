#!/usr/bin/env python3

def ShellSort(list):
    '''
    A shell sort ignores immediate neighbors and instead focuses on elements
    at a fixed distance from one another. In the first iteration, elements at
    a fixed distance are swapped if the former is larger than the latter. The
    distance is then decreased and elements swapped until the distance hits 0
    and the list is sorted.
    '''
    # Start sorting with a fixed distance of half the list's length
    distance = len(list) // 2

    # Distance will decrease with each pass
    while distance > 0:
        # Pass through the second half of the list
        for i in range(distance, len(list)):
            # Save the start value of the list at i
            temp = list[i]
            # j will be iterator that starts at i
            j = i

            # Pass until j near 0 or earlier item smaller than saved value
            while j >= distance and list[j - distance] > temp:
                # Move earlier element to index j
                list[j] = list[j - distance]
                j -= distance

            list[j] = temp
        
        # Reduce the distance for the next element
        distance //= 2

    # Return sorted list
    return list
