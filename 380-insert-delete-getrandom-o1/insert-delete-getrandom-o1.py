class RandomizedSet:

    def __init__(self):
        self.rs = {}
        self.list = []
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.rs:
            return False
        
        self.rs[val] = self.length
        self.length += 1
        self.list.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.rs:
            return False

        idx = self.rs[val]
        last = self.list[-1]
        self.list[idx] = last
        self.rs[last] = idx
        self.list.pop()
        del self.rs[val]
        self.length -= 1
        return True
        
    def getRandom(self) -> int:
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()