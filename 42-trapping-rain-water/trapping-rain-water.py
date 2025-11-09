class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLeft = maxRight = 0
        water = 0

        while l < r:
            if height[l] <= height[r]:
                maxLeft = max(maxLeft, height[l])
                water += max(0, maxLeft - height[l])
                l += 1
            
            else:
                maxRight = max(maxRight, height[r])
                water += max(0, maxRight - height[r])
                r -= 1
        
        return water
        
