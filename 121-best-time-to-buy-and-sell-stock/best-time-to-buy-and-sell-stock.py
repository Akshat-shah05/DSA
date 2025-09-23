class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)

            if prices[r] < prices[l]:
                l = r

            r += 1

        return maxP

        