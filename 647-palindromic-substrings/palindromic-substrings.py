class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i][j] contains True or False, representing if s[i : j + 1] is a palindrome
        # Base Case 1: Individual character --> i.e dp[i][i] = True
        # Base Case 2: Dual Characters --> i.e dp[i][i + 1] = True if s[i] == s[i + 1] else False

        # Recursive case --> dp[i][j] = True if dp[i + 1][j - 1] = True AND s[i] == s[j]
            # Check for all substrings (i.e from length 3 to length N)
        n, ans = len(s), 0
        dp = [[False] * n for _ in range(n)]

        # Setup for Base Case 1
        for i in range(n):
            dp[i][i] = True
            ans += 1
        
        # Setup for Base Case 2
        for i in range(n - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            ans += dp[i][i + 1]
        
        # Recursive Case
        for sLen in range(3, n + 1):
            i = 0
            for j in range(i + sLen - 1, n):
                dp[i][j] = (dp[i + 1][j - 1]) and (s[i] == s[j])
                if dp[i][j]:
                    ans += 1
                i += 1
    
        return ans
