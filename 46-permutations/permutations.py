class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(curr, used):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return
            
            for num in nums:
                if num in used:
                    continue
                used.add(num)
                curr.append(num)
                backtrack(curr, used)
                curr.pop()
                used.remove(num)

        backtrack([], set())
        return ans