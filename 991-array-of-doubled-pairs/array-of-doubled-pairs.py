class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        freqs = defaultdict(int)
        for num in arr:
            freqs[num] += 1
            if num >= 0:
                if num % 2 == 0 and num // 2 in freqs and freqs[num // 2] != 0:
                    freqs[num // 2] -= 1
                    freqs[num] -= 1
                
            else:
                if num * 2 in freqs and freqs[num * 2] != 0:
                    freqs[num * 2] -= 1
                    freqs[num] -= 1
            
        for num, freq in freqs.items():
            if freq > 0:
                return False
        
        return True
    
