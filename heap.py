class Heap:
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0
    def insert(self, val):
        self.heap.append(val)
        self.currentSize = self.currentSize+1
        self.percUp(self.currentSize)
    def percUp(self, i):
        while i//2 > 0:
            if self.heap[i] > self.heap[i//2]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i//2]
                self.heap[i//2] = temp
            i = i//2
    def extract(self):
        if self.currentSize == 0:
            return None
        elif self.currentSize == 1:
            ret_val = self.heap[1]
            self.currentSize = self.currentSize-1
            self.heap = [0]
            return ret_val
        else:
            ret_val = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.currentSize = self.currentSize-1
            self.percDown(1)
            return ret_val
    def percDown(self, i):
        while i <= self.currentSize//2:
            mc = self.getMaxChild(i)
            if self.heap[i] < self.heap[mc]:
                tmp = self.heap[mc]
                self.heap[mc] = self.heap[i]
                self.heap[i] = tmp
            i = mc

    def getMaxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap[i*2] > self.heap[i*2+1]:
                return i*2
            else:
                return i*2+1
    def buildMaxHeap(self, arr):
        self.currentSize = len(arr)
        i = len(arr)//2
        self.heap = [0] + arr[:]
        while(i > 0):
            self.percDown(i)
            i = i-1
    def heapSort(self):
        i = 1
        i = self.currentSize
        ret_arr = []
        while self.heap != [0]:
            top = self.extract()
            ret_arr.insert(0,top)
        return ret_arr
