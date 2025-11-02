class Allocator:

    def __init__(self, n: int):
        self.mem = [0] * n
        self.byId = defaultdict(list)
        self.n = n
        
    def allocate(self, size: int, mID: int) -> int:
        run = 0
        for i in range(self.n):
            if self.mem[i] == 0:
                run += 1
                if run == size:
                    start = i - size + 1
                    self.mem[start:start+size] = [mID] * size
                    self.byId[mID].append((start, size))
                    return start
        
            else:
                run = 0
        
        return -1

    def freeMemory(self, mID: int) -> int:
        if not self.byId[mID]:
            return 0
        
        freed = 0
        for (start, size) in self.byId[mID]:
            self.mem[start:start+size] = [0] * size
            freed += size
        
        del self.byId[mID]
        return freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)