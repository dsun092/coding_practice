import random

class Node:
    def __init__(self, n):
        self.data = n
        self.node = None

    def appendToTail(self, d):
        end = Node(d)
        current = self
        while current.node:
            current = current.node
        current.node = end
    def removeDup(self):
        dupDict = {}
        current = self
        prev = None
        while current:
            if current.data in dupDict:
                if current.node:
                    prev.node = current.node
            else:
                dupDict[current.data] = 1
                prev = current
            current = current.node

    def removeDupInPlace(self):
        current = self
        while current:
            comp = current.node
            prev = current
            while comp:
                if comp.data == current.data:
                    if comp.node:
                        prev.node = comp.node
                    else:
                        prev.node = None
                else:
                    prev = comp
                comp = comp.node
            current = current.node

    def printSelf(self):
        current = self.node
        while current:
            print current.data
            current = current.node


def createRandomLL(l):
    n = Node(random.randrange(0, 20))
    for i in xrange(l):
        n.appendToTail(random.randrange(0,20))
    return n
