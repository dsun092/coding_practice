def find_smallest(arr):
    smallest = arr[0]
    for i in xrange(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
    return smallest

def dumb_sort(arr):
    for i in xrange(0, len(arr)):
        smallest = arr[i]
        smallest_index = i
        for x in xrange(i+1, len(arr)):
            if smallest > arr[x]:
                smallest = arr[x]
                smallest_index = x
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
    print arr

def mergesort(arr):
    if len(arr) <= 1:
        return
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)

        merge(arr, left, right)

def merge(arr, left, right):
    a = 0
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[a] = left[l]
            l = l + 1
        else:
            arr[a] = right[r]
            r = r + 1
        a = a + 1
    while l < len(left):
        arr[a] = left[l]
        a = a+1
        l = l+1
    while r < len(right):
        arr[a] = right[r]
        a = a+1
        r = r+1

def quicksort(arr, left, right):
    if left < right:
        split = partition(arr, left, right)

        quicksort(arr, left, split-1)
        quicksort(arr, split+1, right)

def partition(arr, left, right):
    pivotValue = arr[left]
    leftmark = left+1
    rightmark = right
    done = False

    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotValue:
            leftmark = leftmark + 1
        while arr[rightmark] >= pivotValue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if leftmark > rightmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
    temp = arr[rightmark]
    arr[rightmark] = pivotValue
    arr[left] = temp

    return rightmark

def binarySearch(arr, value):
    mid = len(arr)//2
    left = 0
    right = len(arr)
    while left < right:
        if arr[mid] == value:
            return True
        elif arr[mid] < value:
            left = mid
        else:
            right = mid
        mid = (right+left)//2

def binary_search_recursion(arr, target_value):
    mid = len(arr)//2
    if arr[mid] == target_value:
        return True
    if len(arr) == 1:
        return False
    if arr[mid] > target_value:
        binary_search_recursion(arr[:mid], target_value)
    else:
        binary_search_recursion(arr[mid:], target_value)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_arr = [0, 1]
    for i in xrange(2, n):
        fib_arr.append(fib_arr[i-1]+fib_arr[i-2])
    print fib_arr
    print fib_arr[-1]
