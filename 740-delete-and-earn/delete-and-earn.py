class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        maxVal = max(nums)
        for num in nums:
            points[num] += num
            
        prev2 = 0
        prev1 = points[1]
        curr = prev1

        for i in range(2, maxVal + 1):
            curr = max(prev1, prev2 + points[i])
            prev2, prev1 = prev1, curr
        
        return prev1