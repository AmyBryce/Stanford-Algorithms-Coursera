# Quicksort
import sys

# A = [3, 8, 2, 5, 1, 4, 7, 6]

# Test cases previously posted by learner SzuHsien Lee.
# https://dl.dropboxusercontent.com/u/20888180/AlgI_wk2_testcases/10.txt
# https://dl.dropboxusercontent.com/u/20888180/AlgI_wk2_testcases/100.txt
# https://dl.dropboxusercontent.com/u/20888180/AlgI_wk2_testcases/1000.txt

# Answers are:
# size first last median
# 10 25 29 21
# 100 615 587 518
# 1000 10297 10184 8921

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def findPivot1(A, l, r):
    # always pick the first element as the pivot
    # p = A[l]
    return l

def findPivot2(A, l, r):
    return r - 1

def findPivot3(A, l, r):
    first = l
    last = r - 1
    if (r - l) % 2 == 0:
        middle = l + (r - l)/2 - 1
    else:
        middle = l + (r - l)/2

    # source: http://stackoverflow.com/questions/17158667/minimum-no-of-comparisons-to-find-median-of-3-numbers
    x = A[first] - A[middle]
    y = A[middle] - A[last]
    z = A[first] - A[last]

    if(x * y > 0):
        return middle
    if(x * z > 0):
        return last
    return first

def partition(A, l, r):
    # assume pivot is the first element in array A
    p = A[l]
    i = l + 1

    for j in range(l + 1, r):
        # if A[j] > p; do nothing
        if A[j] < p:
            # swap with A[i]
            # increment i
            swap(A, i, j)
            # tmp = A[i]
            # A[i] = A[j]
            # A[j] = tmp
            i += 1

    # swap the pivot with A[i-1]
    swap(A, i - 1, l)
    # tmp = A[i-1]
    # A[i-1] = A[l]
    # A[l] = tmp

    # p = A[i-1]
    return i - 1

def quicksort(A, l, r, findPivot):
    # base case: subarray length is 1 or 0
    if (r - l == 1) or (r - l == 0):
        return 0

    pivotIndex = findPivot(A, l, r)

    if pivotIndex != l:
        swap(A, pivotIndex, l)

    pivotIndex = partition(A, l, r)

    # when there is a recursive call on a subarray of length m,
    # you should simply add m-1 to your running total of comparisons
    comparisons = (r - l) - 1

    comparisons += quicksort(A, l, pivotIndex, findPivot)
    comparisons += quicksort(A, pivotIndex + 1, r, findPivot)
    return comparisons

f = file(sys.argv[1])
lines = f.readlines()
A = map(int, lines)

print quicksort(A[:], 0, len(A), findPivot1)
print quicksort(A[:], 0, len(A), findPivot2)
print quicksort(A[:], 0, len(A), findPivot3)
# print A
