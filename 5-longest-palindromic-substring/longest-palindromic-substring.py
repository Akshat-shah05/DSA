class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        max_start = 0
        max_length = 1

        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            l += 1
            r -= 1
            
            if (r - l + 1) > max_length:
                max_length = (r - l + 1)
                max_start = l

            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            l += 1
            r -= 1

            if (r - l + 1) > max_length:
                max_length = (r - l + 1)
                max_start = l
        
        print(max_length)
        return s[max_start : max_start + max_length]
