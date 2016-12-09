def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        leftarr = arr[:mid]
        rightarr = arr[mid:]
        mergesort(leftarr)
        mergesort(rightarr)

        i = 0
        j = 0
        k = 0
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i=i+1
            else:
                arr[k] = rightarr[j]
                j=j+1
            k = k+1
        while i < len(leftarr):
            arr[k]=leftarr[i]
            i=i+1
            k=k+1
        while j < len(rightarr):
            arr[k] = rightarr[j]
            j=j+1
            k=k+1

def countInversion(arr):
    if len(arr) <= 1:
        return 0
    else:
        mid = len(arr)/2
        left = arr[:mid]
        right = arr[mid:]
        leftInv = countInversion(left)
        rightInv = countInversion(right)
        split = countSplitInversion(arr, left, right)
        return leftInv + rightInv + split

def countSplitInversion(arr, left, right):
    l = 0
    r = 0
    a = 0
    numL = len(left)
    numR = len(right)
    numInversion = 0

    while l < numL and r < numR:
        if left[l] < right[r]:
            arr[a] = left[l]
            a += 1
            l += 1
        else:
            print left[l], right[r]
            arr[a] = right[r]
            numInversion += numL - l
            r+=1
            a+=1
    while l < numL:
        arr[a] = left[l]
        a +=1
        l +=1
    while r < numR:
        arr[a] = right[r]
        a +=1
        r +=1
    return numInversion
