def quicksort(arr, left, right):
    if left < right:
        split = partition(arr, left, right)
        quicksort(arr, left, split-1)
        quicksort(arr, split+1, right)


def partition(arr, left, right):
    l = left
    r = right
    pivot = arr[pivot_index]
    done = False

    while not done:
        while l <= r and arr[l] <= pivot:
            l += 1
        while r >= l and arr[r] >= pivot:
            r -= 1
        if l < r:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
        else:
            done = True
    temp = arr[pivot_index]
    arr[pivot_index] = arr[r]
    arr[r] = temp
    return r
