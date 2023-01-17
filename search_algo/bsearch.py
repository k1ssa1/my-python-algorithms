# This is a function that performs a binary search on a sorted list

def binary_search(arr, low , high, x):

    # checks if the highest value of the list is bigger than it's lowest
    if high > low:
        mid = (high + low) // 2

        # checks if the target value x is equal to the list middle value
        if arr[mid] == x:
            return mid

        # if the middle value is greater than the target value we only focus on the left half of the list
        elif arr[mid] > x:
            return binary_search(arr ,low, mid - 1, x)
        
        # if the middle value is lower than x we focus on the right half of the list
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return - 1


