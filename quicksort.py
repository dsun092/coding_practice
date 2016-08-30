def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def partition(A, p, r):
    pi = p
    pivot = A[p]
    while p < r:
        while p <= r and A[p] <= pivot:
            p = p + 1
        while A[r] > pivot:
            r = r - 1
        if (p < r):
            temp = A[p]
            A[p] = A[r]
            A[r] = temp
    temp = A[pi]
    A[pi] = A[r]
    A[r] = A[pi]
    pi = r
    return pi


