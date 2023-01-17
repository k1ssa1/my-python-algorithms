# module imports
import bsearch as bs

# defining the list  and the target
arr = [1,3,6,9,12,18]
x = 12

# function calling
result = bs.binary_search(arr, 0, len(arr) - 1, x)

# test message
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
