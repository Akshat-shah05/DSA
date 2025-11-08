class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(openP, closedP, path):
            if openP == closedP == n:
                ans.append(path)
                return
            
            if openP > closedP:
                backtrack(openP, closedP + 1, path + ")")
            
            if openP < n:
                backtrack(openP + 1, closedP, path + "(" )

        backtrack(0, 0, "")
        return ans