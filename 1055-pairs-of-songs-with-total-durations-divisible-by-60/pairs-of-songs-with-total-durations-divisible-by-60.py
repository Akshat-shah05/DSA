class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = defaultdict(int)
        ans = 0

        for i in range(len(time)):
            needed = (60 - time[i] % 60) % 60
            if needed in remainders:
                ans+=remainders[needed]
            
            remainders[time[i] % 60] += 1
    
        return ans
