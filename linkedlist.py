class Node:
    def __init__(self, val):
        self.val = val
        self.child = None
    def getData(self):
        return self.val
    def getNext(self):
        return self.child
    def setNext(self, node):
        self.child = node
    def setData(self, val):
        self.val = val


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.tail is None and self.head is None:
            self.tail = temp
        self.head = temp
    def append(self, item):
        temp = Node(item)
        self.tail.setNext(temp)
        self.tail = temp
    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.getData() == item:
                return True
            cur = cur.getNext()
        return False
    def size(self):
        cur = self.head
        count = 0
        while cur is not None:
            count = count + 1
            cur = cur.getNext()
        return count
    def iterate(self):
        cur = self.head
        while cur is not None:
            print cur.getData()
            cur = cur.getNext()
    def convert(self, arr):
        for i in xrange(0, len(arr)):
            if i == 0:
                self.add(arr[i])
            else:
                self.append(arr[i])

    def remove(self, item):
        cur = self.head
        previous = None
        if cur.getData() == item:
            self.head = cur.getNext()
        else:
            found = False
            while cur.getNext() is not None and not found:
                previous = cur
                cur = cur.getNext()
                if cur.getData() == item:
                    found = True
                    previous.setNext(cur.getNext())
                else:
                    cur = cur.getNext()
