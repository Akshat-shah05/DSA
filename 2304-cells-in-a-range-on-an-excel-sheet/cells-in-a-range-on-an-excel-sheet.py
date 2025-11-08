class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(":")
        startChar, startRow, endChar, endRow = ord(start[0]), int(start[1]), ord(end[0]), int(end[1])

        ans = []
        for char in range(startChar, endChar + 1):
            for i in range(startRow, endRow + 1):
                ans.append(chr(char) + str(i))

        return ans