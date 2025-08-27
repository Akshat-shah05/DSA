from collections import deque

class HitCounter:

    def __init__(self):
        self.hc = deque()
        self.WINDOW = 300

    def hit(self, timestamp: int) -> None:
        if self.hc and self.hc[-1][0] == timestamp:
            self.hc[-1][1] += 1
        
        else:
            self.hc.append([timestamp, 1])
        
        print(self.hc)
        

    def getHits(self, timestamp: int) -> int:
        totalHits = 0
        while self.hc and self.hc[0][0] <= timestamp - self.WINDOW:
            self.hc.popleft()
        
        for timestamp, count in self.hc:
            totalHits += count

        return totalHits
            
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)