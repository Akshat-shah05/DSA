class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        for num in nums:
            points[num] += num
        
        elements = sorted(points.keys())
        prev2 = 0
        prev1 = points[elements[0]]

        for i in range(1, len(elements)):
            cur_elem = elements[i]
            if cur_elem == elements[i - 1] + 1:
                # Then they are adjacent
                prev2, prev1 = prev1, max(prev1, prev2 + points[cur_elem])
            
            else:
                prev2, prev1 = prev1, prev1 + points[cur_elem]
        
        return prev1