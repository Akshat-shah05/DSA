class Solution:
    def countSubstrings(self, s: str) -> int:
        # anything in s at some index i is a palindrome if:
            # s[i] == s[i] (always true)
            # s[i] == s[i + 1] (for i in range(0, len(s) - 1))
        
        # any substring s[i : j + 1] is a palindrome if:
            # s[i] == s[j] and s[i + 1 : j] is a palindrome
        
        # so for ss size of 1 or 2 --> base case calculation
        # for ss size K of 3 --> len(s) --> use ss of size K - 2 to determine if valid
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = True
            ans += 1
        
        for i in range(n - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            ans += dp[i][i + 1]
        
        for sLen in range(3, n + 1):
            i = 0
            for j in range(i + sLen - 1, n):
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
                ans += dp[i][j]
                i += 1
        
        return ans