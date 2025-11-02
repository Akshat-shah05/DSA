class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.exp = {} # -> token -> Expiry time
        self.heap = [] # -> heap of (expiry, token)
    
    def _evict(self, currentTime):
        while self.heap and self.heap[0][0] <= currentTime:
            expiry, tok = heapq.heappop(self.heap)

            if self.exp.get(tok) == expiry:
                del self.exp[tok]
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self._evict(currentTime)
        self.exp[tokenId] = currentTime + self.ttl
        heapq.heappush(self.heap, (currentTime + self.ttl, tokenId))

    def renew(self, tokenId: str, currentTime: int) -> None:
        self._evict(currentTime)
        if tokenId not in self.exp:
            return None
        
        self.exp[tokenId] = currentTime + self.ttl
        heapq.heappush(self.heap, (currentTime + self.ttl, tokenId))

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._evict(currentTime)
        return len(self.exp)
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)