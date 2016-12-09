class Node:
    '''
    Node class has the following properties:
        * key, val pair where key is comparable between nodes
        * left  child
        * right child
        * Red/Black node: 0 for black, 1 for red
        + compare: compares current node key with input key. Return -1, 0, or 1
    '''
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.color = 1

    def compare(self, key):
        '''
        Return -1 if self key is less than input key
        Return 1 if self key is greater than input key
        Return 0 if self key is equals to input key
        '''
        if self.key < key:
            return 1
        elif self.key > key:
            return -1
        else:
            return 0

class BinaryTree:
    '''
    Update 10-14 to RB tree
    '''
    def __init__(self):
        self.root = None

    def get(self, key):
        '''
        Returns the value of node with input key match
        If there are no match, return None
        '''
        node = self.root
        while node != None:
            comp = node.compare(key)
            if comp < 0:
                node = node.left
            elif comp > 0:
                node = node.right
            else:
                return node.val
        return None

    def put(self, key, val):
        '''
        Inserts key, val pair into tree
        '''
        if self.root is None:
            self.root = Node(key, val)
            self.root.color = 0
        else:
            self.root = self._put(self.root, key, val)

    def _put(self, node, key, val):
        '''
        Recursive function to put key, val Node into tree.
        '''
        if node is None:
            return Node(key, val)
        comp = node.compare(key)
        if comp < 0:
            node.left = self._put(node.left, key, val)
        elif comp > 0:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        if node.left.left is not None and self._isRed(node.left.left) == True:
            node = self._rightRotation(node)
        if self._isRed(node.left) == False:
            node = self._leftRotation(node)
        self._colorFlip(node)
        return node

    def minVal(self):
        '''
        returns the value of the smallest key in tree
        '''
        node = self.root
        while node.left is not None:
            node = node.left
        return node.val

    def maxVal(self):
        '''
        returns the value of the largest key in tree
        '''
        node = self.root
        while node.right is not None:
            node = node.right
        return node.val

    def floor(self, key):
        '''
        Returns the largest value where key is <= input key
        '''
        node = self._floor(self.root, key)
        if node is None:
            return None
        return node.val

    def _floor(self, node, key):
        '''
        If node is none, return none
        If input key is less than key at root, we go to left subtree
        If input key is greater than key at root, floor of k is in
            the right subtree
        '''
        if node is None:
            return None
        comp = node.compare(key)
        if comp == 0:
            return node
        elif comp < 0:
            return self._floor(node.left, key)
        subroot = self._floor(node.right, key)
        if subroot is not None:
            return subroot
        else:
            return node

    def ceiling(self, key):
        '''
        Returns the largest value where key is >= input key
        '''
        node = self._ceiling(self.root, key)
        if node is None:
            return None
        return node.val

    def _ceiling(self, node, key):
        if node is None:
            return None
        comp = node.compare(key)
        if comp == 0:
            return node
        elif comp > 0:
            return self._ceiling(node.right, key)
        subtree = self._ceiling(node.left, key)
        if subtree is not None:
            return subtree
        else:
            return node
    def size(self):
        '''
        Returns the size of tree
        '''
        return self._size(self.root)
    def _size(self, node):
        if node is None:
            return 0
        else:
            return node.count

    def rank(self, key):
        '''
        Returns # of keys in tree that are smaller than input key
        '''
        return self._rank(self.root, key)

    def _rank(self, node, key):
        '''
        If node is none return 0
        If node is less than input key, then rank is rank of node's left child
        if node is greater than input key, then rank is
            number of nodes in left subtree + current node + rank of right subtree
        '''
        if node is None:
            return 0
        comp = node.compare(key)
        if comp < 0:
            return self._rank(node.left, key)
        elif comp > 0:
            return 1 + self._size(node.left) + self._rank(node.right, key)
        else:
            return self._size(node.left)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        comp = node.compare(key)
        if comp < 0:
            node.left = self._delete(node.left, key)
        elif comp > 0:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = node
            min_right = node.right
            while min_right.left is not None:
                min_right = min_right.left
            node = min_right
            node.right = self._deleteMin(temp.right)
            node.left = temp.left
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _deleteMin(self, node):
        if node.left is None:
            return node.right
        node.left = self._deleteMin(node.left)
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _leftRotation(self, node):
        if self._isRed(node.right) == True:
            right = node.right
            right.left = node
            node.color = right.color
            right.color = 1
            return right
        return node
    def _rightRotation(self, node):
        if self._isRed(node.left) == True:
            left = node.left
            left.right = node
            node.color = left.color
            left.color = 1
            return left
        return node
    def _colorFlip(self, node):
        if self._isRed(node) == False and self._isRed(node.left) == True and self._isRed(node.right) == True:
            node.color = 1
            node.left.color = 0
            node.right.color = 0

    def _isRed(self, node):
        if node is None:
            return False
        return node.color == 1

    def inordertraversal(self, node):
        '''
        Prints out the values within the tree in ascending order according to
        the keys of the tree.
        '''
        if node is None:
            return
        self.inordertraversal(node.left)
        print node.val
        self.inordertraversal(node.right)

    def reversetraversal(self, node):
        if node is None:
            return
        self.reversetraversal(self, node.right)
        print node.val
        self.reversetraversal(self, node.left)

def constructtree():
    tree = BinaryTree()
    input_nodes = [{50: 'A'}, {10: 'B'}, {5: 'C'}, {17: 'T'}, {84: 'N'}, {56: 'K'}, {90: 'QQ'}, {9: 'Q'}]
    for item in input_nodes:
        for k,v in item.iteritems():
            tree.put(k,v)
    return tree
