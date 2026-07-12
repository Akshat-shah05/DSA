from collections import defaultdict, deque
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []

        for index, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")

            parsed.append((
                name,
                int(time),
                int(amount),
                city,
                index
            ))

        parsed.sort(key=lambda transaction: transaction[1])

        # name -> deque of (time, city, original_index)
        name_to_recent = defaultdict(deque)
        invalid = [False] * len(transactions)

        for name, time, amount, city, index in parsed:
            if amount > 1000:
                invalid[index] = True

            recent = name_to_recent[name]

            # Remove transactions more than 60 minutes old.
            while recent and time - recent[0][0] > 60:
                recent.popleft()

            # Every remaining transaction is within 60 minutes.
            for previous_time, previous_city, previous_index in recent:
                if previous_city != city:
                    invalid[index] = True
                    invalid[previous_index] = True

            recent.append((time, city, index))

        return [
            transactions[index]
            for index in range(len(transactions))
            if invalid[index]
        ]