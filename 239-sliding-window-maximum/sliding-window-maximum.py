class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        ans = []
        q = deque()
        for r in range(len(nums)):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            
            q.append(r)

            if q[0] <= r - k:
                q.popleft()
            
            if r >= k - 1:
                ans.append(nums[q[0]])
        
        return ans