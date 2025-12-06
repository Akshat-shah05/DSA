class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlength = 0
        for num in numset:
            if num - 1 in numset:
                continue
            
            x = num
            length = 1
            while x + 1 in numset:
                x += 1
                length += 1

            maxlength = max(length, maxlength)
        
        return maxlength