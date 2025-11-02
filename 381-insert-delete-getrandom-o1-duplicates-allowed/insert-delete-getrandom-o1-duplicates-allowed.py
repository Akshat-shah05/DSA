from random import choice

class RandomizedCollection:

    def __init__(self):
        self.vals = defaultdict(list)
        self.list = []
        self.length = 0

    def insert(self, val: int) -> bool:
        ans = False if val in self.vals else True
        self.vals[val].append(self.length)
        self.list.append(val)
        self.length += 1

        return ans

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False
        
        idx = self.vals[val][-1]
        self.vals[val].pop()

        if not self.vals[val]:
            del self.vals[val]

        lastElem = self.list[-1]
        self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
        self.list.pop()

        if idx != self.length - 1:
            self.vals[lastElem].remove(self.length - 1)
            self.vals[lastElem].append(idx)

        self.length -= 1

        return True

    def getRandom(self) -> int:
        return choice(self.list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()