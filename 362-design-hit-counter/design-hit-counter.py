class HitCounter:

    def __init__(self):
        self.WINDOW = 300
        self.hitsHistory = deque()

    def hit(self, timestamp: int) -> None:
        if self.hitsHistory and self.hitsHistory[-1][0] == timestamp:
            self.hitsHistory[-1][1] += 1

        else:
            self.hitsHistory.append([timestamp, 1])
        self._prune(timestamp)

    def getHits(self, timestamp: int) -> int:
        self._prune(timestamp)
        total = 0
        for _, count in self.hitsHistory:
            total += count
        
        return total
    
    def _prune(self, timestamp):
        while self.hitsHistory and self.hitsHistory[0][0] + self.WINDOW <= timestamp:
            self.hitsHistory.popleft()
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)