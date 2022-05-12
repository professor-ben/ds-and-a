#!/usr/bin/env python3

def MergeSort(list):
    '''
    A merge sort's performance is not affected by the degree to which the
    input is sorted. The sort will first split the input into two parts
    recursively until the sizes of the "left" and "right" lists are equal.
    These lists are then merged into a sorted list through the use of a while
    loop. Additional while loops then append any unused elements of "left" and
    "right" before returning the sorted list.
    '''
    # Do not run code on list of length < 1
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        # These continue until list length is 1
        MergeSort(left)
        MergeSort(right)

        # a is index of left, b is index of right, x is index of list
        a = 0
        b = 0
        c = 0

        # Continue until a is the length of left or b is the length of right
        while a < len(left) and b < len(right):
            # Add smallest to lowest unmodified index of list
            if left[a] < right[b]:
                list[c] = left[a]
                a += 1
            else:
                list[c] = right[b]
                b += 1
            # Increase as each of right, left, list is used or modified
            c += 1
        
        # Use remainder of left
        while a < len(left):
            list[c] = left[a]
            a += 1
            c += 1
            
        # Use remainder of right
        while b < len(right):
            list[c] = right[b]
            b += 1
            c += 1

    # Return sorted list
    return list
