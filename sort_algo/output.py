import bubble_sort as bs
import merge_sort as ms

# defining the list
unsorted_list = [8,4,3,9,0]
unsorted_list_two = [5,8,4,1]
# function callings
bsort = bs.bubble_sort(unsorted_list)
msort = ms.merge_sort(unsorted_list_two)

print("Sorted list", unsorted_list )
print("Sorted list using merge sort", unsorted_list_two)