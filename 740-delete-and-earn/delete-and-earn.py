class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        maxVal = 0
        for num in nums:
            points[num] += num
            maxVal = max(maxVal, num)
        
        prev2 = 0
        prev1 = points[1]
        curr = prev1

        for i in range(2, maxVal + 1):
            temp = prev1
            curr = max(prev1, prev2 + points[i])
            prev2 = temp
            prev1 = curr
        
        return prev1