from collections import deque

class HitCounter:

    def __init__(self):
        self.hits = deque() # [timestamp, count]
        self.WINDOW = 300

    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        
        else:
            self.hits.append([timestamp, 1])
        
    def getHits(self, timestamp: int) -> int:
        minimumTimeAgo = timestamp - self.WINDOW
        while self.hits and self.hits[0][0] <= minimumTimeAgo:
            self.hits.popleft()
        
        totalHits = 0
        for timestamp, count in self.hits:
            totalHits += count
    
        return totalHits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)