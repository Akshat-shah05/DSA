class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        i = 0
        ans = 0
        while i < n:
            ans += self.loop(i, i, n, s)
            ans += self.loop(i, i + 1, n, s)
            i += 1
        
        return ans
    
    def loop(self, l, r, n, s):
        ans = 0
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        
        return ans