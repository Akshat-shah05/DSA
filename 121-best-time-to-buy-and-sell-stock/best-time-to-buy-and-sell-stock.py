class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        total = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            total = max(profit, total)

            if prices[r] > prices[l]:
                r += 1
            
            else:
                l = r
                r += 1 
        
        return total