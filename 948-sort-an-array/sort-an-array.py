class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        
        mid = n // 2
        
        Left = self.sortArray(nums[:mid])
        Right = self.sortArray(nums[mid:])

        Merged = self.merge(Left, Right)
        return Merged

    def merge(self, L, R):
        merged = []
        i = 0
        j = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                merged.append(L[i])
                i += 1
            
            else:
                merged.append(R[j])
                j += 1
        
        while i < len(L):
            merged.append(L[i])
            i += 1
        
        while j < len(R):
            merged.append(R[j])
            j += 1
        
        return merged

        