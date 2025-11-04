class FrontMiddleBackQueue:

    def __init__(self):
        self.lQ, self.rQ = deque(), deque()
    
    def _rebalance(self):
        while len(self.rQ) > len(self.lQ):
            self.lQ.append(self.rQ.popleft())
        while len(self.lQ) > len(self.rQ) + 1:
            self.rQ.appendleft(self.lQ.pop())

    def pushFront(self, val: int) -> None:
        self.lQ.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.lQ) > len(self.rQ):
            self.rQ.appendleft(self.lQ.pop())
        self.lQ.append(val)
        
    def pushBack(self, val: int) -> None:
        self.rQ.append(val)
        self._rebalance()
        
    def popFront(self) -> int:
        if len(self.lQ) == 0:
            return -1
        
        val = self.lQ.popleft()
        self._rebalance()
        return val
        
    def popMiddle(self) -> int:
        if len(self.lQ) == 0:
            return -1
        
        val = self.lQ.pop()
        self._rebalance()
        return val
        
    def popBack(self) -> int:
        if len(self.rQ) == 0:
            if len(self.lQ) == 0:
                return -1
            
            val = self.lQ.pop()
            self._rebalance()
            return val
        else:
            val = self.rQ.pop()
            self._rebalance()
            return val



# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()