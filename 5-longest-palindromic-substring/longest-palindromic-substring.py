class Solution:
    def longestPalindrome(self, s: str) -> str:
        # every individual character is a palindrome
        # every set of two of the same characters is a palindrome
        # if dp[i][j] represents that s[i : j + 1] is a palindrome
        # Then we know dp[i][j] = s[i] == s[j] && dp[i + 1][j - 1] is True

        # Algorithm
        #   First --> initialize dp array with individual and pairs
        #   Iterate over all substring lengths (3 --> len(s)) --> loop till len(s) + 1
        #   Update each dp[i][j] = s[i] == s[j] && dp[i + 1][j - 1]

        dp = [[False] * (len(s)) for _ in range(len(s))]
        longest = [0, 0]

        for i in range(len(s)):
            dp[i][i] = True
        
        for i in range(len(s) - 1):
            dp[i][i + 1] = True if s[i] == s[i + 1] else False
            if dp[i][i + 1]:
                longest = [i, i + 1]
        
        for sLen in range(3, len(s) + 1):
            i = 0
            for j in range(i + sLen - 1, len(s)):
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j]:
                    longest = [i, j]
                
                i += 1
        
        l, r = longest
        return s[l : r + 1]

