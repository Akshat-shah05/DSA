class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0

        # Base case of just one char
        for i in range(n):
            dp[i][i] = True
            ans += 1
        
        # Base case of two same chars
        for i in range(n - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            ans += dp[i][i + 1]
        
        # All Substring Length
        for sLen in range(3, n + 1):
            i = 0
            for j in range(i + sLen - 1, n):
                dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                ans += dp[i][j]
                i += 1
        
        return ans