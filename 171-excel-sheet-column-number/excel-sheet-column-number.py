class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        val = 0
        rev = columnTitle[::-1]
        factor = 1

        for char in rev:
            val += (ord(char) - ord("A") + 1) * factor
            factor *= 26

        return val