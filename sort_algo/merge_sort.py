def merge_sort(ds):
    #check if the lenth of the list is greater than 1
    if len(ds) > 1:
        # divide and conquer approach
        mid = len(ds) // 2
        # ds left and right partitioning
        L = ds[:mid]
        R = ds[mid:]

        # recursion
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                ds[k] = L[i]
                i += 1
            else:
                ds[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            ds[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            ds[k] = R[j]
            j += 1
            k += 1