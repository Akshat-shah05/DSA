class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber -= 1
            mod = columnNumber % 26
            ans.append(chr(mod + ord("A")))
            columnNumber //= 26
        
        return "".join(ans[::-1])