class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.balance = 0
        self.parent = None
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild
    def getParent(self):
        return self.parent
    def getVal(self):
        return self.val

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size

    def insert(self, val):
        temp = Node(val)
        if self.root is None:
            self.root = temp
        else:
            current = self.root
            parent = None
            found = False
            while not found:
                if val < current.getVal():
                    if current.getLeftChild():
                        parent = current
                        current = current.getLeftChild()
                    else:
                        current.leftChild = temp
                        temp.parent = current
                        self.updateBalance(current.leftChild)
                        found = True
                else:
                    if current.getRightChild():
                        parent = current
                        current = current.getRightChild()
                    else:
                        current.rightChild = temp
                        temp.parent = current
                        self.updateBalance(current.rightChild)
                        found = True
    def updateBalance(self, node):
        if node.balance > 1 or node.balance < -1:
            self.rebalance(node)
        else:
            if node.parent is not None:
                if node.parent.leftChild == node:
                    node.parent.balance = node.parent.balance + 1
                elif node.parent.rightChild == node:
                    node.parent.balance = node.parent.balance - 1
                if node.parent.balance != 0:
                    self.updateBalance(node.parent)

    def rebalance(self, node):
        if node.balance < 0:
            if node.rightChild.balance > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        if node.balance > 0:
            if node.leftChild.balance < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        if rotRoot.parent is None:
            self.root = newRoot
        else:
            if rotRoot.parent.leftChild == rotRoot:
                rotRoot.parent.leftChild = newRoot
            elif rotRoot.parent.rightChild == rotRoot:
                rotRoot.parent.rightChild = newRoot
        newRoot.parent = rotRoot.parent
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balance = rotRoot.balance + 1 - min(newRoot.balance, 0)
        newRoot.balance = newRoot.balance + 1 + max(rotRoot.balance, 0)

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        if rotRoot.parent is None:
            self.root = newRoot
        else:
            if rotRoot.parent.leftChild == rotRoot:
                rotRoot.parent.leftChild = newRoot
            elif rotRoot.parent.rightChild == rotRoot:
                rotRoot.parent.rightChild = newRoot
        newRoot.parent = rotRoot.parent
        rotRoot.parent = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.balance = rotRoot.balance - 1 - max(newRoot.balance, 0)
        newRoot.balance = newRoot.balance - 1 + min(rotRoot.balance, 0)

    def search(self, val):
        if self.root is None:
            return False
        else:
            current = self.root
            while current is not None:
                if current.getVal() == val:
                    return True
                elif val < current.getVal():
                    if current.leftChild:
                        current = current.getLeftChild()
                    else:
                        return False
                elif val > current.getVal():
                    if current.rightChild:
                        current = current.getRightChild()
                    else:
                        return False
        return False
    def getMax(self):
        cur = self.root
        while cur.rightChild is not None:
            cur = cur.rightChild
        return cur.getVal()
    def getMin(self):
        cur = self.root
        while cur.leftChild is not None:
            cur = cur.leftChild
        return cur.getVal()
