# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i = 0
    j = 0
    k = 0
    # Your code here
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k += 1
        i += 1
    
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    if len(arr) > 1:
        mid = len(arr)//2
        A = arr[:mid]
        B = arr[mid:]
        arr = merge(merge_sort(A),merge_sort(B))
    
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    return

def merge_sort_in_place(arr, l, r):
    # Your code here
    return

test_arr1 = [1,4,7]
test_arr2 = [2,3,3]
test_arr3 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
#print(merge(test_arr1,test_arr
#print(merge_sort(test_arr3))