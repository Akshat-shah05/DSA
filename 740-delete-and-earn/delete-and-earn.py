class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        maxVal = 0
        for num in nums:
            points[num] += num
            maxVal = max(num, maxVal)
        
        prev2, prev1 = points[0], points[1]
        curr = 0

        for i in range(2, maxVal + 1):
            curr = max(prev2 + points[i], prev1)
            prev2, prev1 = prev1, curr
        
        return prev1