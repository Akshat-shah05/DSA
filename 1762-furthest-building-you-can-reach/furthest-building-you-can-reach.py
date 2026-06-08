class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        allocated = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            
            if ladders > 0:
                heapq.heappush(allocated, climb)
                ladders -= 1
            
            else:
                smallest_allocated = allocated[0] if allocated else None
                if not smallest_allocated or climb < smallest_allocated:
                    bricks -= climb
                else:
                    heapq.heappop(allocated)
                    heapq.heappush(allocated, climb)
                    bricks -= smallest_allocated
                
                if bricks < 0:
                    return i
        
        return len(heights) - 1

