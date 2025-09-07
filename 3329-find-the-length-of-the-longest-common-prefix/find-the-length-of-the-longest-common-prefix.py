class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixSet = set()
        for num in arr1:
            while num > 0:
                prefixSet.add(num)
                num //= 10
            
        longest = 0
        for num in arr2:
            x = num
            while x > 0 and x not in prefixSet:
                x //= 10
            
            if x != 0:
                longest = max(longest, len(str(x)))
        
        return longest