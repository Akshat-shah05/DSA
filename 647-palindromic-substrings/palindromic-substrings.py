class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(len(s)):
            ans += self.loop(i, i, s, n) + self.loop(i, i + 1, s, n)
        
        return ans
    
    def loop(self, l, r, s, n):
        ans = 0
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        
        return ans