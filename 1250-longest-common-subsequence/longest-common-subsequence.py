class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        memo = {}
        def lcs(i, j):
            if i == n or j == m:
                memo[(i, j)] = 0
                return 0
            
            elif text1[i] == text2[j]:
                if (i, j) not in memo:
                    memo[(i, j)] = 1 + lcs(i + 1, j + 1)
                return memo[(i, j)]
            
            else:
                if (i, j) not in memo:
                    memo[(i, j)] = max(lcs(i + 1, j), lcs(i, j + 1))
                return memo[(i, j)]
        
        ans = lcs(0, 0)
        return ans
            
