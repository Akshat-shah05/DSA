class Solution:
    def jump(self, nums: List[int]) -> int:
        # where dp(i) returns minimum jumps to reach end from ith position
        n = len(nums)
        @cache
        def dp(i):
            if i >= n - 1:
                return 0
            else:
                steps = float('inf')
                for j in range(1, nums[i] + 1):
                    steps = min(steps, dp(i + j) + 1)
                
                return steps
        
        return dp(0)

        