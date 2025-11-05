class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)
        self.prefSum = []
        for i in range(len(w)):
            if i == 0:
                self.prefSum.append(w[i])
            else:
                self.prefSum.append(w[i] + self.prefSum[i - 1])
        
        print(self.prefSum)


    def pickIndex(self) -> int:
        randomNum = random.random() * self.total
        index = bisect_left(self.prefSum, randomNum)
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()