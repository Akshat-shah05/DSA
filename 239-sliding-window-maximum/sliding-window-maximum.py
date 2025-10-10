class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        ans = []
        dq = deque()

        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            
            if i >= k - 1:
                ans.append(nums[dq[0]])
        
        return ans