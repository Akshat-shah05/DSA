class RecentCounter:

    def __init__(self):
        self.WINDOW = 3000
        self.counter = deque()

    def _prune(self, t):
        while self.counter and self.counter[0] + self.WINDOW < t:
            self.counter.popleft()

    def ping(self, t: int) -> int:
        self.counter.append(t)
        self._prune(t)
        return len(self.counter)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)