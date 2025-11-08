class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(openP, closedP, path):
            if openP == closedP == n:
                ans.append(path)
                return
            
            if closedP > openP:
                return 
            
            if openP == n:
                backtrack(openP, closedP + 1, path + ")")
            
            else:
                backtrack(openP + 1, closedP, path + "(")
                backtrack(openP, closedP + 1, path + ")")
            
        backtrack(0, 0, "")
        return ans