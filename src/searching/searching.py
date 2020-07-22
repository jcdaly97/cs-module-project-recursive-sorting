# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, end)
        else:
            return binary_search(arr, target, start, mid -1)
    return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target, descending = False, start = 0, end = -1):
    # Your code here
    if end == -1:
        end = len(arr) -1
    #check for descending
    if arr[start] > arr[end]:
        descending = True
    
    #set a midpoint
    mid = (start + end) // 2

    #case for ascending
    if not descending and start <= end:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return agnostic_binary_search(arr, target, descending, mid + 1, end)
        else:
            return agnostic_binary_search(arr, target, descending, start, mid -1)
    
    #case for descending
    elif descending and start <= end:
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return agnostic_binary_search(arr, target, descending, mid + 1, end)
        else:
            return agnostic_binary_search(arr, target, descending, start, mid -1)
    #failed to find target
    else:
        return -1