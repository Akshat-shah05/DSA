class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l = 0
        ans = 0

        for r in range(len(nums)):
            freq[nums[r]] += 1

            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans