import threading

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.count = 0
        self.capacity = k
        self.headIdx = 0
        self._lock = threading.Lock()

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        with self._lock:
            insertIdx = (self.headIdx + self.count) % self.capacity
            self.q[insertIdx] = value
            self.count += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        with self._lock:
            newHeadIdx = (self.headIdx + 1) % self.capacity
            self.headIdx = newHeadIdx
            self.count -= 1
            return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[self.headIdx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        rearIdx = (self.headIdx + self.count - 1) % self.capacity
        return self.q[rearIdx]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()