# Assumptions:
# 1. List is Sorted
# 2. Left = 0
# 3. Right = length(List)

# Goal: 
#   Return the INDEX! of the key if it exists in the list

# Running Time of BinarySearch(...) == O(logn)

def BinarySearch(A,k,left,right):
    if left > right: 
        return -1
    
    mid = (left + right) // 2

    if k == A[mid]:
        return mid
    elif k < A[mid]:
        return BinarySearch(A, k, left, mid-1)
    else:
        return BinarySearch(A,k, mid+1, right)

assert BinarySearch([1,3,5,7,9], 5, 0, 4) == 2
assert BinarySearch([2,4,6,8,10], 2, 0, 4) == 0
assert BinarySearch([2,4,6,8,10], 10, 0, 4) == 4
assert BinarySearch([1,3,5,7,9], 6, 0, 4) == -1
assert BinarySearch([4], 4, 0, 0) == 0
assert BinarySearch([4], 2, 0, 0) == -1
assert BinarySearch([], 3, 0, -1) == -1
