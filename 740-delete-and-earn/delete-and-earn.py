class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        maxVal = max(nums)
        for num in nums:
            points[num] += num
            
        dp = [0] * (maxVal + 1)
        dp[1] = points[1]

        for i in range(2, maxVal + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
        
        return dp[-1]