from random import choice 

class RandomizedSet:

    def __init__(self):
        self.rs = {}
        self.list = []
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.rs:
            return False
        
        self.rs[val] = self.length
        self.list.append(val)
        self.length += 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.rs:
            return False
        
        idx = self.rs[val]
        lastVal = self.list[-1]
        self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
        self.rs[lastVal] = idx
        del self.rs[val]
        self.list.pop()
        self.length -= 1
        return True

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()