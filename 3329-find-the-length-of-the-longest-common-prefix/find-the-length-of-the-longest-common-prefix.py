class Solution:
    def _allprefixes(self, num):
        ans = []
        while num:
            ans.append(num)
            num //= 10
        
        return ans

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Approach --> Put all the prefixes of each element in arr1 into a hashset
        #          --> Check if the prefixes of each element in arr 2 exists in the hashset

        arr1set = set()
        for num in arr1:
            for prefix in self._allprefixes(num):
                arr1set.add(prefix) 
        
        ans = 0
        for num in arr2:
            x = num
            while x > 0 and x not in arr1set:
                x //= 10
            
            if x != 0:
                ans = max(ans, len(str(x)))
        
        return ans
            
        return ans