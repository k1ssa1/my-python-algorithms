# The time complexity of this code is O(log n^2)

def bubble_sort(ds):
    
    # iterate thru the list
    for i in range(len(ds)):
        # swapping record
        swapped = False
        # element comparaison iteration to compare two elements
        for j in range(0, len(ds) - i - 1):
            # compare the two elements
            if ds[j] > ds[j+1]:
                new_value = ds[j]
                ds[j] = ds[j+1]
                ds[j+1] = new_value

                swapped = True

        if not swapped:
            break
