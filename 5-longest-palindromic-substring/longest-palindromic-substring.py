class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestIdx = [0, 0]
        longestLength = 0
        i = 0

        while i < len(s):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            if (r - l - 1) > longestLength:
                longestLength = r - l - 1
                longestIdx = [l + 1, r - 1]


            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            if (r - l - 1) > longestLength:
                longestLength = r - l - 1
                longestIdx = [l + 1, r - 1]
            
            i += 1
        
        l, r = longestIdx
        return s[l : r + 1]
        