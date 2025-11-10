class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular) + 1
        ans = []

        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = 0
        dp[0][0] = expressCost

        for i in range(1, n):
            dp[i][1] = regular[i - 1] + min(dp[i - 1][1], dp[i - 1][0])
            dp[i][0] = express[i - 1] + min(expressCost + dp[i - 1][1], dp[i - 1][0])

            ans.append(min(dp[i][0], dp[i][1]))
        
        return ans

