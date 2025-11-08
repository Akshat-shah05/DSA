class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([amount])
        seen = set([amount])
        steps = 0

        while q:
            l = len(q)
            for _ in range(l):
                curAmount = q.popleft()
                if curAmount == 0:
                    return steps
                
                for coin in coins:
                    newAmount = curAmount - coin
                    if newAmount >= 0 and newAmount not in seen:
                        seen.add(newAmount)
                        q.append(newAmount)

            steps += 1

        return -1