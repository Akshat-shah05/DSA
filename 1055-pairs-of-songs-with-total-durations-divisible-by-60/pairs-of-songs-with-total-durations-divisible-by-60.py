class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = defaultdict(int)
        ans = 0 

        for t in time:
            if t % 60 == 0:
                ans += remainders[0]
            
            else:
                ans += remainders[60 - t % 60]
            
            remainders[t % 60] += 1
    
        return ans