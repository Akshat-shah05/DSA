class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = defaultdict(int)

        for num in nums:
            modded = (num % value + value) % value
            freq[modded] += 1

        newFreq = freq.copy()
        
        for modded, frequency in freq.items():
            x = value
            f = frequency
            while f > 1:
                newFreq[modded + x] += 1
                f -= 1
                newFreq[modded] -= 1
                x += value
        
        print(newFreq)
        i = 0
        while True:
            if i not in newFreq:
                return i
            
            i += 1


