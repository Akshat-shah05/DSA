class Solution:
    def twoEggDrop(self, n: int) -> int:
        import math
        return math.ceil((math.sqrt(8*n + 1) - 1) / 2)