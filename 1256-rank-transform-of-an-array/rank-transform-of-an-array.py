class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num2rank = {}
        arr2 = sorted(arr)
        seen = set()
        rank = 1

        for num in arr2:
            if num not in seen:
                seen.add(num)
                num2rank[num] = rank
                rank += 1
        
        ans = []

        for num in arr:
            ans.append(num2rank[num])
        
        return ans

