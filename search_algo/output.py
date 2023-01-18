# module imports
import bsearch as bs
import lsearch as ls
# defining the lists and the target
arr = [1,3,6,9,12,18]
x = 12

ds = [1,3,6,9,12,18]
target = 12

# defining the tuple and the target
tup = (10, 20, 30)
z = 20

ds_tuple = [1,3,6,9,12,18]
target_tuple = 3

# binary function calling
result_list = bs.binary_search(arr, 0, len(arr) - 1, x)
result_tuple = bs.binary_search(tup, 0, len(tup) - 1, z)

# linear search function calling
n = len(ds)
linear_search_list = ls.linear_search(ds,n,target)
linear_search_tuple = ls.linear_search(ds_tuple,n,target_tuple)

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


# test message for linear search in a list
if linear_search_list != -1:
    print("Element is present at index", str(linear_search_list), "of the list")
else:
    print("Element is not present in list")

# test message for linear search in a tuple
if linear_search_tuple != -1:
    print("Element is present at index", str(linear_search_tuple), "of the tuple")
else:
    print("Element is not present in tuple")