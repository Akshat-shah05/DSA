class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        needed_matches = m * (k - 1)
        matches = 0
        for i in range(m, len(arr)):
            if arr[i] == arr[i - m]:
                matches += 1

                if matches == needed_matches:
                    return True
            
            else:
                matches = 0
        
        return False