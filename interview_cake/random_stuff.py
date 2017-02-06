class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, inp):
        cur = self.trie
        for char in inp:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]

    def doesExist(self, inp):
        cur = self.trie
        for char in inp:
            if char not in cur:
                return False
            cur = cur[char]
        return True


def find_rotation_point(nums):
    start = 0
    end = len(nums)-1
    mid = len(nums)//2
    while start < end:
        if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
            return mid
        if nums[mid] < nums[start]:
            end = mid-1
            mid = (start+end)//2
        else:
            start = mid+1
            mid = (start+end)//2
    if mid == len(nums)-1:
        return 0
    return mid
