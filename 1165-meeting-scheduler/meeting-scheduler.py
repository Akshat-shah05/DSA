class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        s1p = s2p = 0

        while s1p < len(slots1) and s2p < len(slots2):
            intersect_start = max(slots1[s1p][0], slots2[s2p][0])
            intersect_end = min(slots1[s1p][1], slots2[s2p][1])

            if intersect_start + duration <= intersect_end:
                return [intersect_start, intersect_start + duration]
            
            if slots1[s1p][1] > slots2[s2p][1]:
                s2p += 1
            
            else:
                s1p += 1
        
        return []