class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_heap = [] # a max heap
        sell_heap = [] # a min heap
        for order in orders:
            price, amount, o_type = order
            # BUY Orders
            if o_type == 0: 
                while sell_heap and sell_heap[0][0] <= (price) and amount > 0:
                    _, sell_amount = sell_heap[0]
                    
                    if amount > sell_amount:
                        amount -= sell_amount
                        heapq.heappop(sell_heap)
                    
                    else:
                        remaining = sell_amount - amount
                        amount = 0
                        sell_heap[0][1] = remaining
                
                if amount > 0:
                    heapq.heappush(buy_heap, [-price, amount])
                    
            # SELL Orders
            else:
                while buy_heap and -1 * buy_heap[0][0] >= price and amount > 0:
                    _, buy_amount = buy_heap[0]
                    if amount > buy_amount:
                        amount -= buy_amount
                        heapq.heappop(buy_heap)
                    
                    else:
                        remaining = buy_amount - amount
                        amount = 0
                        buy_heap[0][1] = remaining
                
                if amount > 0:
                    heapq.heappush(sell_heap, [price, amount])
        
        total = 0
        for p, a in buy_heap:
            total += a
        
        for p, a in sell_heap:
            total += a
        
        return total % (10**9 + 7)

