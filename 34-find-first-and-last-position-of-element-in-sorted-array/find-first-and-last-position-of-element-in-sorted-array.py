class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]

        def searchLow():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r)//2
                if nums[mid] >= target:
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            return l
        
        def searchHigh():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r)//2
                if nums[mid] > target:
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            return r
        
        start, end = searchLow(), searchHigh()
        if 0 <= start < len(nums) and start <= end and nums[start] == target:
            return [start, end]
        
        else:
            return [-1, -1]