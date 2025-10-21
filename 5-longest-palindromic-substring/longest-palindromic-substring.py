class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        dp = [[None] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n - 1):
            dp[i][i + 1] = True if s[i] == s[i + 1] else False
            ans = [i, i + 1] if dp[i][i + 1] else ans
        
        for sLen in range(3, n + 1):
            i = 0
            for j in range(sLen + i - 1, n):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j]:
                    ans = [i, j]
                
                i += 1
        
        i, j = ans
        return s[i : j + 1]
        


