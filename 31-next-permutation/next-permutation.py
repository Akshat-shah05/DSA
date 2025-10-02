class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Algorithm
        '''
        find first decreasing element from end of list
        find smallest element from right side thats greater than first decreasing element
        swap these two elements
        reverse sublist from first decreasing to end of list
        '''
        i = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return 
        
        j = len(nums) - 1
        while j >= i and nums[j] <= nums[i - 1]:
            j -= 1
        
        nums[j], nums[i - 1] = nums[i - 1], nums[j]
        nums[i:] = reversed(nums[i:])

        