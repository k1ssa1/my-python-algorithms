# The time complexity of this code is O(log n)
# because the algorithm performs a single pass through the data set of size n
# and in the worst case scenario it compares each element to the target element once
# The time taken to perform the search increases linearly with the size of the data set

def linear_search(ds,n,target):
    for i in range(0,n):
        if (ds[i] == target):
            return i