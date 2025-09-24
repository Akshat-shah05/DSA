class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        heapq.heappush(self.maxHeap, -self.minHeap[0])
        heapq.heappop(self.minHeap)
        
        if len(self.minHeap) < len(self.maxHeap):
            heapq.heappush(self.minHeap, -self.maxHeap[0])
            heapq.heappop(self.maxHeap)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        else:
            return (self.minHeap[0] - self.maxHeap[0]) * 0.5
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()