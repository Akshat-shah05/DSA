class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(ans, openP, closedP):
            if openP == closedP and openP == n:
                result.append(ans)

            
            if openP > closedP:
                backtrack(ans + ")", openP, closedP + 1)
            
            if openP < n:
                backtrack(ans + "(", openP + 1, closedP)
            
        backtrack("", 0, 0)
        return result
            

            
