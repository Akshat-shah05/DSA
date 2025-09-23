class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = defaultdict(int)

        for num in nums:
            modded = (num % value + value) % value
            freq[modded] += 1

        i = 0
        while True:
            r = i % value
            if freq[r] > 0:
                freq[r] -= 1
                i += 1
            
            else:
                return i
        


