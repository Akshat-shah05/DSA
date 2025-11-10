class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        # lets min(dp[i][0], dp[i][1]) represent minimum cost to get to stop i
        costs = []
        n = len(regular)
        baseRegular = 0
        baseExpress = expressCost

        for i in range(1, n + 1):
            temp = baseRegular
            baseRegular = regular[i - 1] + min(baseRegular, baseExpress)
            baseExpress = express[i - 1] + min(temp + expressCost, baseExpress)

            costs.append(min(baseRegular, baseExpress))
        
        return costs

