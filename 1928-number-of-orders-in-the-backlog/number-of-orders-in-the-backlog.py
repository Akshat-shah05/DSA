class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buyHeap = []
        sellHeap = []

        MOD = 10**9 + 7

        for price, amount, orderType in orders:
            if orderType == 0:
                remaining = amount

                while remaining > 0 and sellHeap and sellHeap[0][0] <= price:
                    sell_price, sell_amount = sellHeap[0]
                    minAmount = min(remaining, sell_amount)
                    remaining -= minAmount
                    sell_amount -= minAmount
                    if sell_amount == 0:
                        heapq.heappop(sellHeap)
                    
                    else:
                        sellHeap[0] = (sell_price, sell_amount)

                if remaining >= 0:
                    heapq.heappush(buyHeap, (-price, remaining))
            
            elif orderType == 1:
                remaining = amount

                while remaining > 0 and buyHeap and -buyHeap[0][0] >= price:
                    buy_price, buy_amount = buyHeap[0]
                    minAmount = min(remaining, buy_amount)
                    remaining -= minAmount
                    buy_amount -= minAmount
                    if buy_amount == 0:
                        heapq.heappop(buyHeap)
                    
                    else:
                        buyHeap[0] = (buy_price, buy_amount)

                if remaining > 0:
                    heapq.heappush(sellHeap, (price, remaining))
            
            else:
                raise ValueError("invalid order type")
    

        total = 0
        for _, amt in buyHeap:
            total = (total + amt) % MOD
        for _, amt in sellHeap:
            total = (total + amt) % MOD
        return total