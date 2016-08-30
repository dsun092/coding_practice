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



