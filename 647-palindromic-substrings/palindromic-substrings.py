class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        total = 0
        dp = [[False] * n for _ in range(n)]    
        for i in range(n):
            dp[i][i] = True
            total += 1
        
        for i in range(n - 1):
            dp[i][i + 1] = True if s[i] == s[i + 1] else False
            if dp[i][i + 1]:
                total += 1
        
        for sLen in range(3, n + 1):
            i = 0
            for j in range(i + sLen - 1, n):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j]:
                    total += 1
                
                i += 1
    
        return total