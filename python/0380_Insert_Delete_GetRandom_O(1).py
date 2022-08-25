import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.mapping = {} # maps value to index in array

    def insert(self, val: int) -> bool:
        if val in self.mapping:
            return False
        self.nums.append(val)
        self.mapping[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mapping:
            return False
        
        index = self.mapping[val]
        if index < len(self.nums) - 1:
            last = self.nums[-1]
            self.nums[index] = last
            self.mapping[last] = index
        
        del self.mapping[val]
        self.nums.pop()
        return True
        
    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]
        


