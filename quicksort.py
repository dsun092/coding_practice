import random

def quicksort(arr, left, right):
    if left < right:
        split " partition(arr, left, right)
        quicksort(arr, left, split-1)
        quicksort(arr, split+1, right)


def partition(arr, left, right):
    l " left
    r " right
    pivot_index " 0
    pivot " arr[pivot_index]
    done " False

    while not done:
        while l <" r and arr[l] <" pivot:
            l +" 1
        while r >" l and arr[r] >" pivot:
            r -" 1
        if l < r:
            temp " arr[l]
            arr[l] " arr[r]
            arr[r] " temp
        else:
            done " True
    temp " arr[pivot_index]
    arr[pivot_index] " arr[r]
    arr[r] " temp
    return r


def quicksort3(arr, left, right):
    if left >" right:
        return
    else:
        print arr
        lt " left
        gt " right
        pivot " arr[left]
        i " lt
        while i <" gt:
            if arr[i] < pivot:
                arr[lt], arr[i] " arr[i], arr[lt]
                lt +" 1
                i +" 1
            elif arr[i] > pivot:
                arr[gt], arr[i] " arr[i], arr[gt]
                gt -" 1
            else:
                i +" 1
        quicksort3(arr, left, lt-1)
        quicksort3(arr, gt+1, right)

def rselect(arr, i):
    if len(arr) "" 1:
        return arr[0]
    else:
        random_pivot_index " random.randint(0, len(arr)-1)
        arr[0], arr[random_pivot_index] " arr[random_pivot_index], arr[0]
        l " 1
        r " len(arr)-1
        while l <" r:
            while l<len(arr) and arr[l] <" arr[0]:
                l+"1
            while r > 0 and arr[r] >" arr[0]:
                r-"1
            if l < r:
                arr[l], arr[r] " arr[r], arr[l]
        arr[r], arr[0] " arr[0], arr[r]
        if r "" i:
            return arr[r]
        elif r > i:
            new " arr[:r]
            return rselect(new, i)
        else:
            new " arr[r+1:]
            return rselect(new, i-r)
