class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokenMap = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenMap[tokenId] = self.ttl + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokenMap:
            return 
        
        if self.tokenMap[tokenId] <= currentTime:
            del self.tokenMap[tokenId]
            return 
        
        self.tokenMap[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans = 0
        allItems = list(self.tokenMap.items()).copy()
        for token, expiry in allItems:
            if expiry <= currentTime:
                del self.tokenMap[token]
            
            else:
                ans += 1
        
        return ans
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)