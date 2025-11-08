class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        times = 1
        for char in columnTitle[::-1]:
            ans = times * (ord(char) - ord("A") + 1) + ans
            times *= 26
        
        return ans