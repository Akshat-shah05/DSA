class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = defaultdict(int)

        for i, num in enumerate(nums):
            needed = target - num
            if needed in hmap:
                return [i, hmap[needed]]
            
            hmap[num] = i
            