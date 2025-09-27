class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        maxVal = 0
        for num in nums:
            points[num] += num
            maxVal = max(num, maxVal)
        
        dp = [0] * (maxVal + 1)
        dp[0] = points[0]
        dp[1] = points[1]

        for i in range(2, maxVal + 1):
            dp[i] = max(dp[i - 2] + points[i], dp[i - 1])
        
        return dp[-1]