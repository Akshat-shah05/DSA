class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        # lets min(dp[i][0], dp[i][1]) represent minimum cost to get to stop i
        costs = []
        n = len(regular)
        dp = [[0, 0] for _ in range(n + 1)]
        dp[0][0] = 0
        dp[0][1] = expressCost

        for i in range(1, n + 1):
            dp[i][0] = regular[i - 1] + min(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = express[i - 1] + min(dp[i - 1][0] + expressCost, dp[i - 1][1])

            costs.append(min(dp[i][0], dp[i][1]))
        
        return costs


