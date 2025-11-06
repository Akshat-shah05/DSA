class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num2rank = {}
        arr2 = sorted(arr)
        rank = 1

        for i in range(len(arr2)):
            if i > 0 and arr2[i] > arr2[i - 1]:
                rank += 1
            num2rank[arr2[i]] = rank
        
        ans = []

        for num in arr:
            ans.append(num2rank[num])
        
        return ans

