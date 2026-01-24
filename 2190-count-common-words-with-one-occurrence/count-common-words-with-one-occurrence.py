class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for word in words1:
            map1[word] += 1
        
        for word in words2:
            map2[word] += 1
        
        ans = 0
        
        for key, val in map1.items():
            if val == 1 and map2[key] == 1:
                ans += 1
        
        return ans