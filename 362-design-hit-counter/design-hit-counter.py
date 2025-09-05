class HitCounter:

    def __init__(self):
        self.WINDOW = 300
        self.hitsHistory = deque()

    def hit(self, timestamp: int) -> None:
        self.hitsHistory.append(timestamp)
        self._prune(timestamp)

    def getHits(self, timestamp: int) -> int:
        self._prune(timestamp)
        return len(self.hitsHistory)
    
    def _prune(self, timestamp):
        while self.hitsHistory and self.hitsHistory[0] + self.WINDOW <= timestamp:
            self.hitsHistory.popleft()
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)