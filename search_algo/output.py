# module imports
import bsearch as bs

# defining the list and the target
arr = [1,3,6,9,12,18]
x = 12

# defining the tuple and the target
tup = (10, 20, 30)
z = 20

# function calling
result_list = bs.binary_search(arr, 0, len(arr) - 1, x)
result_tuple = bs.binary_search(tup, 0, len(tup) - 1, z)

# test message for list
if result_list != -1:
    print("Element is present at index", str(result_list), "of the list")
else:
    print("Element is not present in list")

# test message for tuple
if result_tuple != -1:
    print("Element is present at index", str(result_tuple), "of the tuple")
else:
    print("Element is not present in tuple")
