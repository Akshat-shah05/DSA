class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        s1 = s2 = 0

        while s1 < len(slots1) and s2 < len(slots2):
            intersect_start = max(slots1[s1][0], slots2[s2][0])
            intersect_end = min(slots1[s1][1], slots2[s2][1])

            if intersect_start + duration <= intersect_end:
                return [intersect_start, intersect_start + duration]
            
            if slots1[s1][1] >= slots2[s2][1]:
                s2 += 1
            
            else:
                s1 += 1
        
        return []